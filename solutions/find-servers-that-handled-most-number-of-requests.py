# ============================================================
#  Problem : Find Servers That Handled Most Number of Requests
#  URL     : https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
#  Solution: https://leetcode.com/solutions/find-servers-that-handled-most-requests-bj9t0/
#  Date    : 2026-11-09
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Request i must go to server i % k, or the next free server after it in cyclic order. A direct scan works, but it is O(n·k) and times out when many servers are busy. The fix is to stop scanning: keep the free servers in sorted order so the next free one can be found with a binary search, and keep the busy servers in a heap so finished ones can be released cheaply.

# Approach
1. Keep `free`, a sorted list of free server ids (initially 0 to k-1).
2. Keep `busy`, a min-heap of `(end_time, server)`.
3. For each request, first pop every busy server whose `end_time <= arrival[i]` and put it back into `free` with `insort`, which keeps the list sorted.
4. If `free` is empty, every server is busy, so the request is dropped.
5. Otherwise use `bisect_left(free, i % k)` to find the first free server at or after the preferred one. If the position runs past the end, wrap around to index 0.
6. Remove that server from `free`, increment its count, and push `(arrival[i] + load[i], server)` onto `busy`.
7. At the end, return every server whose count equals the maximum.

My first version scanned servers one by one starting from i % k. It was correct but got Time Limit Exceeded on 105 of 108 test cases, because with k around 30,000 most servers were busy and each request walked past a long run of them.

# Complexity
- Time complexity: $$O(n \log k)$$ for the heap and binary-search operations. `insort` and `pop` on a Python list are $$O(k)$$ memory shifts, but they are very fast in practice.
- Space complexity: $$O(k)$$, for the free list, the busy heap and the counts.

# Code

# --- CODE ---
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = list(range(k))        # sorted list of free server ids
        busy = []                    # min-heap of (end_time, server)
        count = [0] * k

        for i in range(len(arrival)):
            # release servers that have finished by now
            while busy and busy[0][0] <= arrival[i]:
                _, s = heapq.heappop(busy)
                insort(free, s)

            if not free:
                continue             # all busy: request dropped

            pos = bisect_left(free, i % k)
            if pos == len(free):
                pos = 0              # wrap around
            server = free.pop(pos)

            count[server] += 1
            heapq.heappush(busy, (arrival[i] + load[i], server))

        most = max(count)
        return [s for s in range(k) if count[s] == most]

