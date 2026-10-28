# ============================================================
#  Problem : Best Time to Buy and Sell Stock
#  URL     : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#  Solution: https://leetcode.com/solutions/python-track-min-price-one-pass-on-by-sa-vvui/
#  Date    : 2026-10-19
#  Author  : Sanskar_phougat
# ============================================================

# ----- WRITE-UP -----
# Intuition
For any selling day, the best day to have bought is the cheapest day before it. So I don't need to compare every pair of days. I only need to remember the lowest price seen so far.

# Approach
1. Keep `minprice`, starting at infinity, and `maxprofit`, starting at 0.
2. Go through the prices once. For each price, update `minprice` to the smaller of the current `minprice` and this price.
3. Compute the profit if I sold today, `price - minprice`, and update `maxprofit` if it's larger.
4. Return `maxprofit`. It stays 0 when prices only fall, which matches the requirement to return 0 when no profit is possible.

# Complexity
- Time complexity: $$O(n)$$. Each price is visited exactly once.
- Space complexity: $$O(1)$$. Only two variables are used, no matter how large the input is.

# Code

# ----- CODE -----
class Solution:
    def maxProfit(self, prices):
        minprice=float('inf')
        maxprofit=0
        for i in prices:
            minprice=min(minprice, i )
            maxprofit=max(maxprofit, i - minprice)
        return maxprofit
