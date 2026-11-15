# ============================================================
#  Problem : Subsets II
#  URL     : https://leetcode.com/problems/subsets-ii/
#  Solution: https://leetcode.com/solutions/backtracking-sort-skip-duplicates-pick-n-4h10/
#  Date    : 2026-11-15
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
This is the same pick/not-pick backtracking as Subsets, but `nums` may contain duplicates. If we run the plain Subsets solution, we'd generate duplicate subsets (e.g., `[1,2]` twice from `[1,2,2]`). To avoid this, we **sort** the array first so duplicates are adjacent, then during the "exclude" step we skip all consecutive duplicates at once.

# Approach
1. **Sort** `nums` (done once at `i == 0`) so duplicates sit next to each other.
2. At each index `i`:
   - **Pick:** add `nums[i]`, recurse with `i + 1`, then pop (backtrack).
   - **Not-pick:** find `j` — the first index after `i` where `nums[j] != nums[i]` — and recurse from `j`, skipping the whole duplicate block.

This guarantees each unique subset is generated exactly once.

# Complexity
- Time complexity: $$O(n \cdot 2^n)$$ — at most $2^n$ subsets, each copied in $O(n)$.
- Space complexity: $$O(n)$$ — recursion depth + current subset (excluding output).

# Code
```python3
class Solution:
    def subsetsWithDup(self, nums: list[int], i=0, ans=None, result=None) -&gt; list[list[int]]:
        if ans is None:
            ans = []
        if result is None:
            result = []
        if i == 0:
            nums.sort()

        if (i == len(nums)):
            result.append(ans[:])
            return result

        ans.append(nums[i])
        self.subsetsWithDup(nums, i+1, ans, result)
        ans.pop()

        j = i + 1
        while j &lt; len(nums) and nums[j] == nums[i]:
            j += 1
        self.subsetsWithDup(nums, j, ans, result)

        return result

# --- CODE ---


