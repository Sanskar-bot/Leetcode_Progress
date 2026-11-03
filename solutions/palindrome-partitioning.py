# ============================================================
#  Problem : Palindrome Partitioning
#  URL     : https://leetcode.com/problems/palindrome-partitioning/
#  Solution: https://leetcode.com/solutions/backtracking-cut-where-the-piece-is-a-pa-1trk/
#  Date    : 2026-11-01
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
A partition is a way of cutting the string into pieces. I build it one piece at a time: from the current start position, try every possible piece, and only continue with pieces that are palindromes. A piece that is not a palindrome can never be part of a valid partition, so that branch is dropped immediately.

# Approach
1. Keep a shared list `path` of pieces chosen so far, and a result list `res`.
2. `backtrack(start)` builds the partition from position `start` onwards.
3. If `start == len(s)`, the whole string is used, so save a copy of `path` and return.
4. Otherwise, for every `i` from `start + 1` to `len(s)`, take `part = s[start:i]`. If it is a palindrome, append it, call `backtrack(i)` (the next piece begins where this one ended), then pop it to undo.
5. Start with `backtrack(0)` and return `res`.

# Complexity
- Time complexity: $$O(n \cdot 2^n)$$ in the worst case (for example `"aaaa"`, where every cut is valid), since there can be up to 2^(n-1) partitions and each costs O(n) to build and copy.

- Space complexity: $$O(n)$$ for the recursion depth and `path`, not counting the output.

# Code

# --- CODE ---
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res=[]
        path=[]

        def ispalin(test):
            return test == test[::-1]

        def backtrack(start):
            if (start == len(s)):
                res.append(path[:])
                return 
            for i in range (start+1 , len(s)+1):
                part=s[start:i]
                if ispalin(part):
                    path.append(part)
                    backtrack(i)
                    path.pop()
        backtrack(0)
        return res

