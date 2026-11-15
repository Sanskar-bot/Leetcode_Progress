# ============================================================
#  Problem : Subsets
#  URL     : https://leetcode.com/problems/subsets/
#  Solution: https://leetcode.com/solutions/backtracking-pick-or-not-pick-includeexc-c6sg/
#  Date    : 2026-11-15
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
The problem asks for all possible subsets (the power set) of `nums`. This is a classic backtracking problem: for each element, we have two choices — either **include** it in the current subset or **exclude** it. Making both choices recursively over all elements generates every possible subset, which is exactly `2^n` of them.

# Approach
We use backtracking (pick / not-pick):

1. If `i == len(nums)`, we've processed every element — save a copy of the current subset `ans` into `result` and return.
2. **Pick:** add `nums[i]` to `ans`, recurse with `i + 1`, then **pop** it back out (backtrack).
3. **Not-pick:** recurse with `i + 1` without adding anything.

Note: since Python's default mutable arguments are shared across calls, we initialize `ans` and `result` to fresh lists inside the function when they are `None`.

# Complexity
- Time complexity: $$O(n \cdot 2^n)$$ — there are $2^n$ subsets, and copying each subset of up to size $n$ takes $O(n)$.
- Space complexity: $$O(n)$$ — recursion depth plus the current subset (excluding the output, which holds $2^n$ subsets).

# Code
```python3
class Solution:
    def subsets(self, nums: list[int], ans=None, i=0, result=None) -&gt; list[list[int]]:
        if ans is None:
            ans = []
        if result is None:
            result = []
        if (i == len(nums)):
            result.append(ans[:])
            return result

        ans.append(nums[i])
        self.subsets(nums, ans, i+1, result)
        ans.pop()
        self.subsets(nums, ans, i+1, result)

        return result

# --- CODE ---


