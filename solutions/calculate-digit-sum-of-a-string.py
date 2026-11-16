# ============================================================
#  Problem : Calculate Digit Sum of a String
#  URL     : https://leetcode.com/problems/calculate-digit-sum-of-a-string/
#  Solution: https://leetcode.com/solutions/simulation-round-based-digit-sum-groupin-5jjr/
#  Date    : 2026-11-16
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
We repeatedly replace `s` with the digit sum of each group of `k` consecutive digits until the length of `s` is less than or equal to `k`. Since the string shrinks quickly (each round reduces length roughly by a factor of `k`), a simple simulation works efficiently.

# Approach
While the length of `s` is greater than `k`:

1. Scan the string left to right, accumulating the sum of digits.
2. Every time we've processed `k` digits (`(i + 1) % k == 0`) or reached the last character, append the accumulated sum to a new string `String` and reset the sum.
3. After the loop, set `s = String` and repeat.

When `len(s) &lt;= k`, return `s`.

# Complexity
- Time complexity: $$O(n \cdot \log_k n)$$ — each round is $O(n)$, and the string length drops by a factor of about $k$ each round, so there are $O(\log_k n)$ rounds.
- Space complexity: $$O(n)$$ — for the intermediate string in each round.

# Code
```python3
class Solution:
    def digitSum(self, s: str, k: int) -&gt; str:
        String = ""
        Sum = 0
        while len(s) &gt; k:
            for i in range(len(s)):
                Sum += int(s[i])
                if ((i + 1) % k == 0) or i == len(s) - 1:
                    String += str(Sum)
                    Sum = 0
            s = String
            String = ""
        return s

# --- CODE ---


