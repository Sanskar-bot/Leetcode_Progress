# ============================================================
#  Problem : Happy Number
#  URL     : https://leetcode.com/problems/happy-number/
#  Solution: https://leetcode.com/solutions/happy-number-digit-square-recursion-stop-0g9s/
#  Date    : 2026-11-09
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Repeatedly replacing a number with the sum of the squares of its digits either reaches 1 (happy) or loops forever (unhappy). So the real question is how to detect the loop without storing every number seen.

# Approach
1. If n is 1, return True.
2. If n is 4, return False. Every unhappy number eventually falls into the cycle 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4, so reaching 4 means it will never reach 1.
3. Otherwise, compute the sum of the squares of n's digits and recurse on that value.

A "stop at single digits" shortcut fails because 7 is happy: 7 → 49 → 97 → 130 → 10 → 1.

# Complexity
- Time complexity: $$O(\log n)$$ per step, since each step processes the digits of n. The number of steps is small and bounded, because values quickly drop below 243 and then enter either 1 or the cycle.
- Space complexity: $$O(1)$$ extra space apart from the recursion stack, whose depth is bounded by a small constant.

# Code

# --- CODE ---
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 4:
            return False
        answer=0
        while(n):
            answer+=(n%10)**2
            n=n//10
        return self.isHappy(answer)

