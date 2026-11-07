# ============================================================
#  Problem : Trapping Rain Water
#  URL     : https://leetcode.com/problems/trapping-rain-water/
#  Solution: https://leetcode.com/solutions/trapping-rain-water-two-pointers-o1-spac-e4km/
#  Date    : 2026-11-07
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Trapping Rain Water | LeetCode 42

## Intuition

The amount of water trapped above any bar depends on the maximum height of the bars on its left and right sides.

For every position, the water trapped is determined by the smaller of these two boundaries.

The formula is:

Water at index i = min(MaxLeft, MaxRight) - height[i]

Instead of calculating the maximum left and right heights separately for every position, we can use the **Two Pointers technique** to solve the problem efficiently.

## Approach

1. Initialize two pointers:
   - `left` at the beginning of the array.
   - `right` at the end of the array.

2. Maintain two variables:
   - `left_max`: Maximum height encountered from the left.
   - `right_max`: Maximum height encountered from the right.

3. Compare the heights at the two pointers:
   - If `height[left] < height[right]`, process the left side.
   - Otherwise, process the right side.

4. While processing a side:
   - If the current height is greater than or equal to its corresponding maximum, update the maximum.
   - Otherwise, the difference between the maximum boundary and current height represents the trapped water.

5. Move the corresponding pointer inward and continue until both pointers meet.

### Key Observation

When the left boundary is smaller than the right boundary, we can safely calculate the water trapped at the left position because the right boundary is already tall enough to support the water level determined by the left maximum.

The same reasoning applies symmetrically to the right side.

This allows us to calculate trapped water in a single traversal without using additional arrays.

## Complexity

- **Time Complexity:** O(n), since each pointer moves through the array at most once.
- **Space Complexity:** O(1), since we only use a constant number of variables regardless of the input size.

# Code

# --- CODE ---
class Solution:
    def trap(self, height: list[int]) -> int:

        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water

