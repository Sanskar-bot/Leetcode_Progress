# ============================================================
#  Problem : String to Integer (atoi)
#  URL     : https://leetcode.com/problems/string-to-integer-atoi/
#  Solution: https://leetcode.com/solutions/single-pass-parse-lstrip-sign-digits-cla-y3xy/
#  Date    : 2026-11-07
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
The problem is a step-by-step parsing job: skip leading spaces, read an optional sign, read digits until something that isn't a digit appears, then clamp the result to the 32-bit range. Following those rules in order handles every case, including empty strings and strings with no digits.

# Approach
- Use `s.lstrip()` to remove leading spaces only. Spaces in the middle must stay, because they stop the number (`"1 2"` gives `1`).
- If the string is now empty, return `0`.
- Check the first character for a sign: `-` sets `sign = -1`, `+` keeps `sign = 1`. In both cases, set `start = 1` to skip the sign character.
- Loop over `s[start:]` and build the number with `total = total * 10 + digit`, using a dictionary to convert each character to its digit.
- Stop at the first non-digit character with `break`.
- Multiply by `sign` and clamp the result to `[-2^31, 2^31 - 1]` using `max(-2**31, min(2**31 - 1, total))`.

# Complexity
- Time complexity:
$$O(n)$$, where $$n$$ is the length of the string. We scan it at most once (`lstrip` and the digit loop are both linear).

- Space complexity:
$$O(n)$$ in the worst case, because `lstrip()` and `s[start:]` create new strings. Everything else is $$O(1)$$.

# Code

# --- CODE ---
class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
        s = s.lstrip()              # skip leading spaces only
        if not s:                   # empty string -> 0
            return 0

        sign = 1
        start = 0
        if s[0] == '-':
            sign = -1
            start = 1               # skip the sign character
        elif s[0] == '+':
            start = 1

        total = 0
        for i in s[start:]:
            if i in numbers:
                total = total * 10 + numbers[i]
            else:
                break               # stop at first non-digit

        total *= sign
        return max(-2**31, min(2**31 - 1, total))   # clamp to 32-bit range

