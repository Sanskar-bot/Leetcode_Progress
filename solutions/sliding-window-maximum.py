# ============================================================
#  Problem : Sliding Window Maximum
#  URL     : https://leetcode.com/problems/sliding-window-maximum/
#  Solution: https://leetcode.com/solutions/monotonic-deque-on-time-ok-space-python-66tft/
#  Date    : 2026-10-28
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Checking `max()` on every window costs O(k) per window, which is too slow. Instead, I keep a deque of indices whose values are in decreasing order. The front of the deque is always the maximum of the current window, so I can read it in O(1).

# Approach
1. Keep a deque `dq` of indices, with `nums[dq[0]] > nums[dq[1]] > ...` (decreasing values, front to back).
2. For each index `i`:
   - If the front index is outside the window (`dq[0] <= i - k`), pop it from the left.
   - While the back of the deque holds a value smaller than `nums[i]`, pop it. Those elements are older and smaller, so they can never be a window maximum again.
   - Append `i` to the deque.
   - Once `i >= k - 1`, the first window is full, so append `nums[dq[0]]` to the answer.
3. Return the answer list.

# Complexity
- Time complexity: $$O(n)$$, because each index is pushed once and popped at most once.

- Space complexity: $$O(k)$$, because the deque holds at most k indices (the output list is not counted).

# Code

# --- CODE ---
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        out = []
        dq = deque()  # stores indices; their values are in decreasing order

        for i in range(len(nums)):
            # 1. remove the index that fell out of the window
            if dq and dq[0] <= i - k:
                dq.popleft()
                #print ("loop 1 : ", dq , i , "      number at ", i , "is" , nums[i] )

            # 2. remove smaller values from the back, they can never be a max
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
                #print ("loop 2 : ", dq , i , "      number at ", i , "is" , nums[i])

            # 3. add the current index
            dq.append(i)
            #print ("Append ", dq , i , "      number at ", i , "is" , nums[i])

            # 4. once the first window is full, the front is the max
            if i >= k - 1:
                out.append(nums[dq[0]])
                #print ("If i > k-1 : ", dq , i , out ,"      number at ", i , "is" , nums[i])

        return out

