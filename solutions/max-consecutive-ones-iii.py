# ============================================================
#  Problem : Max Consecutive Ones III
#  URL     : https://leetcode.com/problems/max-consecutive-ones-iii/
#  Solution: https://leetcode.com/solutions/sliding-window-count-zeros-on-time-o1-sp-wdp6/
#  Date    : 2026-10-29
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Flipping at most `k` zeros means I am really looking for the longest window that contains at most `k` zeros. Every zero inside such a window can be flipped to 1, so the whole window becomes consecutive ones.

# Approach
1. Keep two pointers `left` and `right`, a counter `zeros` for the zeros inside the window, and `best` for the longest valid window.
2. For each `right`, expand the window. If `nums[right]` is 0, increase `zeros`.
3. While `zeros > k`, the window is invalid, so shrink it from the left. If the element leaving is 0, decrease `zeros`, then move `left` forward.
4. After the window is valid again, update `best` with `right - left + 1`.
5. Return `best`.

`left` can never pass `right`, because an empty window has 0 zeros, which is never greater than `k`.

# Complexity
- Time complexity: $$O(n)$$, because `left` and `right` each move across the array at most once.

- Space complexity: $$O(1)$$, because only a few variables are used.

# Code

# --- CODE ---
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        best = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:              # too many zeros, shrink
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left + 1)

        return best

