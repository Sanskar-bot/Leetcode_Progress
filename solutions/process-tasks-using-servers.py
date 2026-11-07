# ============================================================
#  Problem : Process Tasks Using Servers
#  URL     : https://leetcode.com/problems/process-tasks-using-servers/
#  Solution: https://leetcode.com/solutions/two-min-heaps-free-and-busy-servers-onm-qjjsq/
#  Date    : 2026-11-07
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Each task must go to the free server with the smallest weight (ties broken by smallest index). If no server is free, the task waits until the earliest busy server finishes. That calls for two priority queues: one to pick the best free server, and one to find which busy server frees up first.

# Approach
- Keep a min-heap `free` of `(weight, index)` for idle servers.
- Keep a min-heap `busy` of `(free_at, weight, index)` for servers in use.
- Keep a clock `t`. Task `j` can't start before time `j`, so `t = max(t, j)`.
- If `free` is empty, jump `t` straight to `busy[0][0]` instead of ticking second by second.
- Move every server with `free_at <= t` from `busy` back into `free`.
- Pop the best server from `free`, record its index, and push it into `busy` with `free_at = t + task`.

# Complexity
- Time complexity:
$$O((n + m)\log n)$$, where $$n$$ is the number of servers and $$m$$ the number of tasks. Building the heap is $$O(n)$$ and each task does a constant number of heap operations.

- Space complexity:
$$O(n)$$ for the two heaps (the result list adds $$O(m)$$).

# Code

# --- CODE ---
import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]   # (weight, index)
        heapq.heapify(free)
        busy = []                                         # (free_at, weight, index)
        result = []
        t = 0

        for j, task in enumerate(tasks):
            t = max(t, j)                  # task j arrives at time j

            if not free:                   # everyone busy: jump ahead
                t = max(t, busy[0][0])

            while busy and busy[0][0] <= t:   # release finished servers
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)     # lowest weight, then lowest index
            result.append(i)
            heapq.heappush(busy, (t + task, w, i))

        return result

