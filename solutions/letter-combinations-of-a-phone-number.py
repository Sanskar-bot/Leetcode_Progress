# ============================================================
#  Problem : Letter Combinations of a Phone Number
#  URL     : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#  Solution: https://leetcode.com/solutions/backtracking-one-letter-per-digit-python-24k3/
#  Date    : 2026-11-01
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Each digit maps to a few letters, and a combination picks exactly one letter per digit. That is a decision at every position in `digits`, so I can build the string one letter at a time and undo each choice to try the next letter. This is backtracking: choose, recurse, undo.

# Approach
1. If `digits` is empty, return `[]`.
2. Store the letters for each digit in `value`, padded so that `value[2]` is `abc`, `value[3]` is `def`, and so on.
3. `backtrack(pos)` fills position `pos`. If `len(path) == len(digits)`, every digit has a letter, so save `"".join(path)` and return.
4. Otherwise, loop over the letters of `digits[pos]`: append the letter, call `backtrack(pos + 1)`, then pop it to undo.
5. Start with `backtrack(0)` and return `result`.

# Complexity
- Time complexity: $$O(4^n \cdot n)$$, since each digit has at most 4 letters, giving at most 4^n combinations, and joining each one takes O(n).

- Space complexity: $$O(n)$$ for the recursion depth and `path`, not counting the output.

# Code

# --- CODE ---
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        result=[]
        path=[]
        value=[[], [] ,['a','b','c'] , ['d','e','f'] , ['g','h','i'] , ['j','k','l'] , ['m','n','o'] , ['p','q','r','s'] , ['t','u','v'] , ['w','x','y','z'] ]

        def backtrack( digit , digits ,value):
            if (len(path) == len(digits)):
                result.append("".join(path))
                return
            for i in value[int(digits[digit])]:
                path.append(i)
                backtrack(digit+1 , digits , value)
                path.pop()
        
        backtrack(0, digits, value)
        return result

