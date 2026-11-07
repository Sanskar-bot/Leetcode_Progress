# ============================================================
#  Problem : Valid Palindrome II
#  URL     : https://leetcode.com/problems/valid-palindrome-ii/
#  Solution: https://leetcode.com/solutions/two-pointers-try-skipping-left-or-right-sla6c/
#  Date    : 2026-11-08
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Compare characters from both ends with two pointers. The first time two characters differ, one of them must be the character we delete, but we don't know which. So we try both choices: delete the left character, or delete the right character. If either choice lets the rest of the string match, the answer is `True`.

# Approach
- Write a helper `check(skip_left)` that runs a two-pointer scan with `left = 0`, `right = len(s) - 1` and one deletion available (`life = 1`).
- While `left < right`:
  - If `s[left] == s[right]`, move both pointers inward.
  - If they differ and `life == 0`, return `False`, because the deletion is already used.
  - If they differ and `life == 1`, use the deletion and move only one pointer: `left += 1` when `skip_left` is `True`, otherwise `right -= 1`.
- If the loop ends, the string is a palindrome after at most one deletion, so return `True`.
- Run `check(True)` and `check(False)`, and return `check(True) or check(False)`.

# Complexity
- Time complexity:
$$O(n)$$, where $$n$$ is the length of the string. Each `check` is a single pass with two pointers, and we run it twice.

- Space complexity:
$$O(1)$$, since only a few integer variables are used.

# Code

# --- CODE ---
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(skip_left):
            left = 0
            right = len(s) - 1
            life = 1

            while left < right:
                if s[left] != s[right]:
                    if life == 0:
                        return False
                    life -= 1
                    if skip_left:
                        left += 1          # delete s[left]
                    else:
                        right -= 1         # delete s[right]
                else:
                    left += 1
                    right -= 1
            return True

        return check(True) or check(False)

