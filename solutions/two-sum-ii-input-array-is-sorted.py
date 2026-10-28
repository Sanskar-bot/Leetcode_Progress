# ============================================================
#  Problem : Two Sum II - Input Array Is Sorted
#  URL     : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#  Solution: https://leetcode.com/solutions/two-pointers-on-time-o1-space-python-by-2zmfn/
#  Date    : 2026-10-28
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
The array is already sorted, so I can use the order to decide which pointer to move. If the sum of two numbers is too small, I need a bigger number. If it's too big, I need a smaller one.

# Approach
1. Put one pointer `left` at the start and one pointer `right` at the end.
2. Compute `total = numbers[left] + numbers[right]`.
3. If `total == target`, return `[left + 1, right + 1]` (the problem is 1-indexed).
4. If `total < target`, move `left` forward to get a bigger sum.
5. If `total > target`, move `right` backward to get a smaller sum.
6. Repeat while `left < right`, so the same element is never used twice.

Each step discards one element that cannot be part of the answer, so we never check every pair.

# Complexity
- Time complexity: $$O(n)$$, because the pointers only move toward each other and each element is visited at most once.

- Space complexity: $$O(1)$$, because only two pointers and one variable are used.

# Code

# --- CODE ---
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        right , left = len(numbers)-1 , 0

        while left < right :
            total=numbers[left]+ numbers[right]
            if( total == target):
                return [left + 1, right + 1] 
            elif total < target :
                left+=1
            else:
                right-=1

