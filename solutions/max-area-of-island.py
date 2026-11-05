# ============================================================
#  Problem : Max Area of Island
#  URL     : https://leetcode.com/problems/max-area-of-island/
#  Solution: https://leetcode.com/solutions/dfs-returning-island-size-mark-visited-o-83zp/
#  Date    : 2026-11-03
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
An island is a group of connected land cells, so its area is the number of cells in that group. If I start a DFS from one land cell, it visits every cell of that island, and each cell can contribute 1 to the area. Doing this from every unvisited land cell and keeping the largest result gives the answer.

# Approach
1. `dfs(r, c)` returns the size of the island that includes cell `(r, c)`.
2. If the cell is outside the grid, or is not land, return 0 (base case).
3. Otherwise, mark the cell as visited by overwriting it on the grid, so it is never counted twice.
4. Return `1 +` the results of the four neighbors (down, up, right, left). The 1 counts the current cell.
5. Loop over every cell. When a cell is land, call `dfs` on it and keep the maximum area seen in `maxarea`.
6. Return `maxarea`.

Each call builds its answer from its neighbors' answers, the same "return a value from the children" idea as tree depth.

# Complexity
- Time complexity: $$O(R \cdot C)$$, where `R` and `C` are the number of rows and columns, because each cell is visited at most once.

- Space complexity: $$O(R \cdot C)$$ in the worst case for the recursion stack, when one island fills the whole grid.

# Code

# --- CODE ---
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        row=len(grid)
        column=len(grid[0])
        maxarea=0

        def dfs(r , c ):
            if (r>=row or r<0) or (c>=column or c<0):
                #print("i am out ",r ,c)
                return 0
            if grid[r][c] !=1:
                #print("i am zero ",r ,c)
                return 0
            grid[r][c] = '#'
            #print("i am at ",r ,c)
            a=dfs(r+1 , c )
            b=dfs(r-1 , c )
            s=dfs(r , c+1 )
            d=dfs(r , c-1 )
            return 1+(a+b+s+d)

        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1:
                    #print("entered " ,r,c)
                    area=dfs(r, c)
                    if area>maxarea:
                        maxarea = area
        return maxarea

