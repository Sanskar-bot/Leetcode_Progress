# ============================================================
#  Problem : Valid Sudoku
#  URL     : https://leetcode.com/problems/valid-sudoku/
#  Solution: https://leetcode.com/solutions/valid-sudoku-row-column-and-box-trackers-qxjm/
#  Date    : 2026-11-09
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
A Sudoku board is valid if no digit repeats in any row, column or 3×3 box. So while scanning the board once, I only need to remember which digits I've already seen in each row, each column and each box.

# Approach
1. Create three `defaultdict(list)` trackers: `dictrow`, `dictcol` and `dictbox`.
2. Write a helper `boxnumber(i, j)` that maps a cell to one of the 9 boxes (1 to 9).
3. Scan every cell. If it is `"."`, skip it, because an empty cell can't break a rule.
4. For a filled cell, check whether its digit is already in its row, column or box. If it is, return `False`.
5. Otherwise record the digit in all three trackers and move on.
6. If the whole board is scanned with no duplicate, return `True`.

Empty cells have to be skipped before the duplicate check. If they fall into the same branch as a duplicate, any board with an empty cell gets rejected.

# Complexity
- Time complexity: $$O(1)$$, since the board is always 9×9, so at most 81 cells are visited (or $$O(n^2)$$ for an n×n board).
- Space complexity: $$O(1)$$, since the trackers hold at most 81 digits in total (or $$O(n^2)$$ for an n×n board).

# Code

# --- CODE ---
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        x = 9   
        dictrow = defaultdict(list)
        dictcol = defaultdict(list)
        dictbox = defaultdict(list)

# Populate keys from 1 to x
        for i in range(1, x + 1):
            dictrow[i]
            dictcol[i]
            dictbox[i]
        def boxnumber(i , j):
            y=0
            if( i>=1 and i<=3):
                if(j>=1 and j<=3):
                    y=1
                if(j>=4 and j<=6):
                    y=2
                if(j>=7 and j<=9):
                    y=3
            if( i>=4 and i<=6):
                if(j>=1 and j<=3):
                    y=4
                if(j>=4 and j<=6):
                    y=5
                if(j>=7 and j<=9):
                    y=6
            if( i>=7 and i<=9):
                if(j>=1 and j<=3):
                    y=7
                if(j>=4 and j<=6):
                    y=8
                if(j>=7 and j<=9):
                    y=9
            return y
        
        for i in range(1, 10):
            for j in range(1, 10):
                val = board[i-1][j-1]
                if val == ".":
                    continue                      # empty cell: nothing to check
                n = boxnumber(i, j)
                if val in dictrow[i] or val in dictcol[j] or val in dictbox[n]:
                    return False                  # duplicate found
                dictrow[i].append(val)
                dictcol[j].append(val)
                dictbox[n].append(val)
        return True
        return True

