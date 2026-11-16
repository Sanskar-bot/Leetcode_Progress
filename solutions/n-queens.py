# ============================================================
#  Problem : N-Queens
#  URL     : https://leetcode.com/problems/n-queens/
#  Solution: https://leetcode.com/solutions/backtracking-row-by-row-queen-placement-nx2qk/
#  Date    : 2026-11-16
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
We place queens row by row. Since each row must contain exactly one queen, we track which column each queen occupies (`cols[k] = column of queen in row k`). A position is safe if no previously placed queen shares the same column or diagonal.

# Approach
We use backtracking row by row:

1. If `row == n`, all rows are filled — convert the board to the required string format and add to `res`.
2. For each column `i` in the current row:
   - Check `issafe(row, i)`: no queen in column `i` or on either diagonal (`abs(row - r) == abs(col - c)` for any previous row `r`).
   - Place the queen (`board[row][i] = "Q"`), record the column, and recurse to `row + 1`.
   - Backtrack: remove the queen (`board[row][i] = "."`) and pop the column record.

The diagonal check works because two queens are on the same diagonal iff their row distance equals their column distance.

# Complexity
- Time complexity: $$O(n!)$$ — the first row has $n$ choices, the second at most $n-1$, etc. (upper bound; pruned by safety checks).
- Space complexity: $$O(n)$$ — recursion depth plus the `cols` list (excluding output).

# Code
```python3
class Solution:
    def solveNQueens(self, n: int) -&gt; list[list[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = []          # cols[k] = column of the queen in row k

        def issafe(row, col):
            for r in range(row):           # only the queens already placed
                c = cols[r]
                if c == col or abs(row - r) == abs(col - c):
                    return False
            return True

        def queen(board, row, n):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for i in range(n):
                if issafe(row, i):
                    board[row][i] = "Q"
                    cols.append(i)
                    queen(board, row + 1, n)
                    board[row][i] = "."
                    cols.pop()

        queen(board, 0, n)
        return res

# --- CODE ---


