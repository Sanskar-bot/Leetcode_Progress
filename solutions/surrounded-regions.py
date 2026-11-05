# ============================================================
#  Problem : Surrounded Regions
#  URL     : https://leetcode.com/problems/surrounded-regions/
#  Solution: https://leetcode.com/solutions/dfs-from-the-border-mark-safe-cells-flip-71zo/
#  Date    : 2026-11-03
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
It is hard to decide which regions are surrounded, but easy to decide which are safe: a region is safe if any of its `O` cells is on the border. So I search from the border, mark everything reachable as safe, and whatever `O` remains must be surrounded.

# Approach
1. `dfs(r, c)` stops if the cell is outside the board or is not `'O'`. A visited cell is marked `'#'`, so it is no longer `'O'` and is never visited twice.
2. Otherwise, mark the cell `'#'` and recurse in the four directions.
3. Call `dfs` from every `'O'` on the border (first and last row, first and last column). This marks every `O` connected to the edge.
4. Flip every remaining `'O'` to `'X'`, since it was never reached and is surrounded.
5. Turn every `'#'` back into `'O'`.

The order of steps 4 and 5 matters: restoring before flipping would turn the safe cells into `X`. The number of separate regions does not matter, because each border search marks its own whole region.

# Complexity
- Time complexity: $$O(R \cdot C)$$, because each cell is marked at most once and the board is scanned a constant number of times.

- Space complexity: $$O(R \cdot C)$$ in the worst case for the recursion stack.

# Code

# --- CODE ---
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        row = len(board) 
        column = len(board[0])

        def dfs (r,c):
            if (r>= row or r<0) or (c>=column or c<0):
                #print ("at the edge ",r,c)
                return 
            if board[r][c] != 'O':
                return 
        
            board[r][c]='#'
            dfs(r+1 , c)
            dfs(r-1 , c)
            dfs(r , c+1)
            dfs(r , c-1)

        for r in range (row):
            for c in range (column):
                #print("trying to entering eddge with ",r, c)
                if (c==0 or c==column-1 or r==0 or r==row-1) and board[r][c] == 'O':
                    #print("entering eddge",r, c)
                    dfs(r,c)

        for r in range(row):
            for c in range(column):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'

