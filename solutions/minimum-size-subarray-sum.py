# ============================================================
#  Problem : Minimum Size Subarray Sum
#  URL     : https://leetcode.com/problems/minimum-size-subarray-sum/
#  Solution: https://leetcode.com/solutions/sliding-window-on-time-o1-space-python-b-ie0d/
#  Date    : 2026-10-28
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
All numbers are positive, so adding an element to the window can only increase the sum, and removing one can only decrease it. That means I can grow a window on the right until its sum reaches the target, then shrink it from the left to find the shortest valid length.

# Approach
1. Keep two pointers `left` and `right`, a running sum `total`, and `minlen` starting at infinity.
2. For each `right`, add `nums[right]` to `total` (expand the window).
3. While `total >= target`:
   - Update `minlen` with the current window length `right - left + 1`.
   - Subtract `nums[left]` from `total`, then move `left` forward (shrink the window).
4. After the loop, return `0` if `minlen` is still infinity (no valid subarray exists), otherwise return `minlen`.

Shrinking while the window is still valid is safe because a longer window with the same right end can never beat a shorter one.

# Complexity
- Time complexity: $$O(n)$$, because `left` and `right` each move across the array at most once.

- Space complexity: $$O(1)$$, because only a few variables are used.

# Code

# --- CODE ---
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        total = 0
        minlen = float('inf')

        for right in range (len(nums)):
            total+=nums[right]
            while total>=target:
                minlen=min(minlen , right - left +1 )
                total-=nums[left]
                left+=1
                

        return 0 if minlen == float('inf') else minlen

