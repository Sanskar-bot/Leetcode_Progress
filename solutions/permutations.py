# ============================================================
#  Problem : Permutations
#  URL     : https://leetcode.com/problems/permutations/
#  Solution: https://leetcode.com/solutions/backtracking-with-swap-on-n-or-in-place-y56o5/
#  Date    : 2026-11-16
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
We need all possible orderings of `nums`. This is a classic backtracking problem: build each permutation one position at a time. When we've filled all positions (i.e., `start == len(nums)`), we've found a complete permutation — save it and backtrack.

# Approach
We use backtracking with index swapping:

1. If `start == len(nums)`, append a copy of `nums` to `res` and return.
2. For each index `i` from `start` to `len(nums) - 1`:
   - **Swap** `nums[start]` and `nums[i]` — place `nums[i]` at the current position.
   - **Recurse** with `start + 1` to fill the rest.
   - **Swap back** (backtrack) to restore the original state for the next iteration.

This generates every permutation exactly once without extra memory for a "used" array.

# Complexity
- Time complexity: $$O(n \cdot n!)$$ — there are $n!$ permutations, and copying each takes $O(n)$.
- Space complexity: $$O(n)$$ — recursion depth (excluding the output which holds $n!$ permutations).

# Code
```python3
class Solution:
    def permute(self, nums: list[int]) -&gt; list[list[int]]:
        res = []

        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # backtrack (swap back)

        backtrack(0)
        return res

# --- CODE ---


