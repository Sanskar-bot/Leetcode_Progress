# ============================================================
#  Problem : Find First and Last Position of Element in Sorted Array
#  URL     : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#  Solution: https://leetcode.com/solutions/find-first-and-last-position-of-element-8koyv/
#  Date    : 2026-11-09
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
The array is sorted, so binary search can find the target in O(log n). But a plain binary search returns any match, and I need the first and last positions. Finding one match and then walking outward fails on inputs like [8,8,8,8,8], where the walk is O(n). So instead of stopping at a match, I keep searching toward the edge I care about.

# Approach
1. Write a helper `find(first)` that runs a normal binary search with `lo`, `hi` and `ans = -1`.
2. If `nums[mid] < target`, move `lo = mid + 1`. If `nums[mid] > target`, move `hi = mid - 1`.
3. If `nums[mid] == target`, save `ans = mid` instead of returning, then keep looking:
   - for the first position, set `hi = mid - 1` to check further left
   - for the last position, set `lo = mid + 1` to check further right
4. When the loop ends, `ans` holds the leftmost (or rightmost) match, or -1 if the target never appeared.
5. Return `[find(True), find(False)]`.

My first attempt found one match and then walked left and right one step at a time. It passed the sample cases but failed LeetCode's restrictions check, because the walk is O(n) on arrays full of the same value.

# Complexity
- Time complexity: $$O(\log n)$$, since each of the two searches halves the range every step.
- Space complexity: $$O(1)$$, since only a few integer variables are used.

# Code

# --- CODE ---
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def find(first):
            lo = 0
            hi = len(nums) - 1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    ans = mid              # remember it, but keep looking
                    if first:
                        hi = mid - 1       # look for an earlier one
                    else:
                        lo = mid + 1       # look for a later one
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return ans

        return [find(True), find(False)]

