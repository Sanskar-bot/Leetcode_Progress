# ============================================================
#  Problem : Climbing Stairs II
#  URL     : https://leetcode.com/problems/climbing-stairs-ii/
#  Solution: https://leetcode.com/solutions/climbing-stairs-ii-bottom-up-dp-look-bac-sg7l/
#  Date    : 2026-11-11
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
The cheapest way to reach step j depends only on the cheapest way to reach the three steps before it, because the last jump was 1, 2 or 3 steps long. A greedy "pick the cheapest next jump" fails because it ignores where that jump leads, so I store the best cost for every step and build up from step 0.

# Approach
1. Let `dp[j]` be the minimum total cost to reach step j. Set `dp[0] = 0` and every other entry to infinity.
2. For each step j from 1 to n, try every jump size d in 1, 2, 3 where `j - d >= 0`.
3. Arriving from step `j - d` costs `dp[j - d] + costs[j - 1] + d * d`. The `j - 1` is because `costs` is 1-indexed in the problem but 0-indexed in Python.
4. Keep the smallest of those options in `dp[j]`.
5. Return `dp[n]`.

My first attempt was greedy. It picked the cheapest jump from each step and then moved on to step i + 1 instead of the step it had jumped to, so it added a cost for every step, including steps the path skips. Looking backwards from the step being reached, and comparing all routes, fixes both problems.

# Complexity
- Time complexity: $$O(n)$$, since each step checks at most 3 previous steps.
- Space complexity: $$O(n)$$, for the `dp` array.

# Code

# --- CODE ---
class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0                                  # start, no cost

        for j in range(1, n + 1):
            for d in range(1, 4):                  # last jump was 1, 2 or 3 steps
                if j - d >= 0:
                    dp[j] = min(dp[j], dp[j - d] + costs[j - 1] + d * d)

        return dp[n]

