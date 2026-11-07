# ============================================================
#  Problem : Roman to Integer
#  URL     : https://leetcode.com/problems/roman-to-integer/
#  Solution: https://leetcode.com/solutions/right-to-left-scan-add-or-subtract-by-ru-dfj7/
#  Date    : 2026-11-07
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
Roman numerals are normally written from largest to smallest, so symbols add up. The exception is a subtractive pair like `IV` or `IX`, where a smaller symbol comes before a larger one. If you read the string from right to left, you can spot these easily: a symbol smaller than the largest one seen so far must be subtracted, otherwise it is added.

# Approach
- Store the symbol values in a dictionary: `I=1, V=5, X=10, L=50, C=100, D=500, M=1000`.
- Keep `total = 0` and `high = 1`, where `high` is the largest value seen so far from the right.
- While `s` is not empty, look at the last character `s[-1]`:
  - If its value is `>= high`, add it to `total` and update `high`.
  - If its value is `< high`, it is a subtractive case, so subtract it from `total`.
- Remove the last character with `s = s[:-1]` and repeat.
- Return `total`.

# Complexity
- Time complexity:
$$O(n^2)$$ in the strict sense, because `s = s[:-1]` creates a new string on every loop. Since a Roman numeral has at most 15 characters, this is tiny in practice. Using `reversed(s)` instead of slicing makes it $$O(n)$$.

- Space complexity:
$$O(n)$$ for the temporary string created by slicing, plus $$O(1)$$ for the fixed-size dictionary.

# Code

# --- CODE ---
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        high = 1
        total = 0
        while s:
            if roman[s[-1]] >= high:
                total += roman[s[-1]]
                high = roman[s[-1]]

            if roman[s[-1]] < high:
                total -= roman[s[-1]]
            s = s[:-1]

        return total

