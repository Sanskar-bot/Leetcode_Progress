# ============================================================
#  Problem : Binary Search
#  URL     : https://leetcode.com/problems/binary-search/
#  Solution: https://leetcode.com/solutions/binary-search-iterative-with-lohi-pointe-908u/
#  Date    : 2026-11-09
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
The array is sorted, so checking the middle element tells me which half the target can be in. The other half can be thrown away, and repeating that shrinks the search range quickly.

# Approach
1. Keep two pointers, `lo` and `hi`, marking the part of the array still worth searching. Start with the whole array: `lo = 0`, `hi = len(nums) - 1`.
2. While `lo <= hi`, take `mid = (lo + hi) // 2`.
3. If `nums[mid] == target`, return `mid`.
4. If `target > nums[mid]`, the target can only be on the right, so set `lo = mid + 1`.
5. Otherwise it can only be on the left, so set `hi = mid - 1`.
6. If the loop ends, the range is empty and the target isn't in the array, so return `-1`.

I first tried a recursive version that slices the list. Slicing makes the returned index relative to the slice, so the offset has to be added back, and each slice copies the list. Moving `lo` and `hi` over the original array avoids both problems.

# Complexity
- Time complexity: $$O(\log n)$$, since the search range halves on every step.
- Space complexity: $$O(1)$$, since only a few integer variables are used.

# Code

# --- CODE ---
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                lo = mid + 1      # discard the left half
            else:
                hi = mid - 1      # discard the right half

        return -1                 # range is empty: not found

