# ============================================================
#  Problem : Find Minimum in Rotated Sorted Array
#  URL     : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#  Solution: https://leetcode.com/solutions/find-minimum-in-rotated-sorted-array-bin-stl3/
#  Date    : 2026-11-10
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
A rotated sorted array is two sorted runs glued together, and the minimum sits at the point where the values drop. Comparing the middle element with the last element tells me which side of the middle that drop is on, so I can throw away half the range each step.

# Approach
1. Set `low = 0` and `high = len(nums) - 1`.
2. While `low < high`, take `mid = (low + high) // 2`.
3. If `nums[mid] > nums[high]`, the drop point (and so the minimum) must be to the right of `mid`, so set `low = mid + 1`.
4. Otherwise `mid` could itself be the minimum, or the minimum is to its left, so set `high = mid`. I keep `mid` here instead of using `mid - 1`.
5. When `low == high`, only one candidate is left, so return `nums[low]`.

My first attempt tracked the smallest `nums[mid]` seen so far and compared `nums[mid]` with `nums[low]`. When `mid == low`, that comparison is always false, so it discarded the right half, including the real minimum, and failed on `[2,1]`. Comparing against `nums[high]` avoids that, because the right end always reveals which side the drop is on.

# Complexity
- Time complexity: $$O(\log n)$$, since the search range halves on every step.
- Space complexity: $$O(1)$$, since only a few integer variables are used.

# Code

# --- CODE ---
class Solution:
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:   # min is to the right of mid
                low = mid + 1
            else:                        # min is at mid or to the left
                high = mid
        return nums[low]

        return mini

