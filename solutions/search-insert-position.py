# ============================================================
#  Problem : Search Insert Position
#  URL     : https://leetcode.com/problems/search-insert-position/
#  Solution: https://leetcode.com/solutions/search-insert-position-binary-search-ret-m3gw/
#  Date    : 2026-11-10
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
The array is sorted, so binary search can find the target in O(log n). The twist is what to return when the target is missing. When the loop ends, the pointers have crossed, and the spot between them is exactly where the target belongs.

# Approach
1. Set `low = 0` and `high = len(nums) - 1`.
2. While `low <= high`, take `mid = (low + high) // 2`.
3. If `nums[mid] == target`, return `mid`.
4. If `target > nums[mid]`, the target belongs further right, so set `low = mid + 1`.
5. Otherwise it belongs further left, so set `high = mid - 1`.
6. When the loop ends, `low` has moved past every element smaller than the target and `high` sits before every element larger than it, with `low = high + 1`. So `low` is the insert position, and I return it.

My first attempt used special checks for the edges and compared `nums[mid-1]` and `nums[mid+1]`. That went out of bounds and returned the wrong index when the target equalled the last element. Dropping the special cases and returning `low` handled all of them, including a target smaller than everything, larger than everything, and a single-element array.

# Complexity
- Time complexity: $$O(\log n)$$, since the search range halves on every step.
- Space complexity: $$O(1)$$, since only a few integer variables are used.

# Code

# --- CODE ---
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low=0
        high=len(nums)-1
        ans=0


        while low<=high:
            mid=(low+high) //2
            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                low = mid + 1      # discard the left half
            else:
                high = mid - 1 
        return low

