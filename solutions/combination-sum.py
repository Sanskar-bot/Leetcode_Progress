# ============================================================
#  Problem : Combination Sum
#  URL     : https://leetcode.com/problems/combination-sum/
#  Solution: https://leetcode.com/solutions/two-pointers-switch-heads-onm-time-o1-sp-0m97/
#  Date    : 2026-10-31
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Pick a number, subtract it from the target, and solve the smaller problem of making the remaining sum. If the remaining sum reaches 0, the numbers picked form a valid combination. If it goes below 0, that choice was too big, so undo it and try another. This is backtracking: choose, recurse, undo.

# Approach
1. Keep a shared list `prt` of the numbers chosen so far, and a result list `res`.
2. `backtrack(start, remaining)` tries every candidate from index `start` onwards.
3. If `remaining == 0`, save a copy of `prt` and return. If `remaining < 0`, return.
4. For each `i` from `start`: append `candidates[i]`, call `backtrack(i, remaining - candidates[i])`, then pop it to undo.
5. Passing `i` (not `i + 1`) lets the same number be used again. Never going back to an index below `start` stops `[2,2,3]` and `[2,3,2]` from both being counted.
6. Optionally, sort the candidates and `break` when a candidate exceeds `remaining` to skip dead ends.

# Complexity
- Time complexity: $$O(n^{t/m})$$ in the worst case, where `t` is the target and `m` is the smallest candidate, since the recursion can go `t/m` levels deep with up to `n` choices each. The problem guarantees fewer than 150 answers.

- Space complexity: $$O(t/m)$$ for the recursion depth and the `prt` list, not counting the output.

# Code

# --- CODE ---
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        prt=[]

        def backtrack(start , remaining):
            if remaining==0:
                res.append(prt[:])
                return 
            if remaining<0:
                return 
            for i in range (start , len(candidates)):
                prt.append(candidates[i])
                backtrack(i , remaining - candidates[i])
                prt.pop()
        backtrack(0 , target)
        return res

