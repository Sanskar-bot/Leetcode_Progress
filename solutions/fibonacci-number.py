# ============================================================
#  Problem : Fibonacci Number
#  URL     : https://leetcode.com/problems/fibonacci-number/
#  Solution: https://leetcode.com/solutions/python-recursion-memoization-on-time-and-iqa7/
#  Date    : 2026-11-15
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition

The Fibonacci sequence is defined as:

- F(0) = 0
- F(1) = 1
- F(n) = F(n - 1) + F(n - 2), for n >= 2

A direct recursive solution calculates the same Fibonacci numbers repeatedly. For example, calculating `fib(5)` requires `fib(3)` through both `fib(4)` and `fib(3)`.

We can avoid this repeated work using memoization: store each calculated result in a dictionary and reuse it whenever needed.

# Approach

Use recursion with a dictionary called `memo` to store previously calculated Fibonacci numbers.

1. If `memo` is `None`, initialize an empty dictionary for the current top-level call.
2. If `n <= 1`, return `n` directly.
3. If `n` already exists in `memo`, return the stored result.
4. Otherwise, recursively calculate `fib(n - 1)` and `fib(n - 2)`, passing the same dictionary to both calls.
5. Store their sum in `memo[n]` and return it.

Using `memo=None` instead of `memo={}` prevents the dictionary from being shared across independent calls.

# Complexity

- Time complexity: O(n)
  
  Starting with an empty cache, each Fibonacci number from 2 through n is calculated once. Later requests for the same number use an average O(1) dictionary lookup.

- Space complexity: O(n)
  
  The memoization dictionary stores O(n) results, and the recursive call stack can reach O(n) depth.

# Code

```python3
class Solution:
    def fib(self, n: int, memo=None) -> int:
        if memo is None:
            memo = {}

        if n <= 1:
            return n

        if n in memo:
            return memo[n]

        memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)

        return memo[n]
```

# --- CODE ---


