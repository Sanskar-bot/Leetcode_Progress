# ============================================================
#  Problem : Valid Parentheses
#  URL     : https://leetcode.com/problems/valid-parentheses/
#  Solution: https://leetcode.com/solutions/python-stack-hashmap-on-by-sanskar_phoug-8uc7/
#  Date    : 2026-10-19
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
A bracket string is valid only if the most recently opened bracket is the first one to be closed. That last-in, first-out behavior is exactly what a stack does.

# Approach
1. Create an empty `stack` and a dictionary `pairs` that maps each closing bracket to its matching opening bracket.
2. Loop through each character of the string.
3. If the character is a closing bracket (a key in `pairs`), check that the stack isn't empty and that its top equals the matching opener. If not, return `False`. If it matches, pop the opener.
4. Otherwise it's an opening bracket, so push it onto the stack.
5. After the loop, the string is valid only if the stack is empty, since any leftover opener was never closed.

# Complexity
- Time complexity: $$O(n)$$. Each character is processed once, and each push or pop takes constant time.
- Space complexity: $$O(n)$$ in the worst case, for example `"((((("`, where every character is pushed onto the stack.
# Code

# --- CODE ---
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in pairs: 
                if not stack or stack[-1] != pairs[i]:
                    return False
                stack.pop() 
            else:
                stack.append(i)

        return len(stack)==0

