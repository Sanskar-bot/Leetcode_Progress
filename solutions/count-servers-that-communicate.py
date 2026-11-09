# ============================================================
#  Problem : Count Servers that Communicate
#  URL     : https://leetcode.com/problems/count-servers-that-communicate/
#  Solution: https://leetcode.com/solutions/count-servers-that-communicate-rowcolumn-algu/
#  Date    : 2026-11-09
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
A server can communicate if at least one other server shares its row or its column. So instead of comparing servers pairwise, I only need to know how many servers are in each row and each column.

# Approach
1. Make two dictionaries, `dictrow` and `dictcol`, to store how many servers are in each row and column.
2. First pass: for every cell with a 1, increment the count for its row and its column.
3. Second pass: for every cell with a 1, count it if its row count is greater than 1 or its column count is greater than 1.

I used two passes instead of summing the row and column counts directly, because summing would count a server twice when it shares both a row and a column with others.

# Complexity
- Time complexity: $$O(m \cdot n)$$, since the grid is traversed twice.
- Space complexity: $$O(m + n)$$, for the row and column count dictionaries.

# Code

# --- CODE ---
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        dictrow={i: 0 for i in range(len(grid))}
        dictcol={i: 0 for i in range(len(grid[0]))}
        for i in range (row):
            for j in range (col):
                if grid[i][j] == 1:
                    dictrow[i] += 1
                    dictcol[j] += 1
        total = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (dictrow[i] > 1 or dictcol[j] > 1):
                    total += 1
        return total

