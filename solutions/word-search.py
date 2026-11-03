# ============================================================
#  Problem : Word Search
#  URL     : https://leetcode.com/problems/word-search/
#  Solution: https://leetcode.com/solutions/backtracking-on-a-grid-mark-visited-rest-h6t6/
#  Date    : 2026-11-01
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Intuition
To find the word, I try every cell as a starting point and match the word one letter at a time, moving to a horizontal or vertical neighbor for each next letter. A cell cannot be used twice, so I mark the cell I am standing on and unmark it when I leave. That is backtracking: choose, recurse, undo.

# Approach
1. `search(r, c, k)` answers: "standing on cell (r, c), can I match the word from letter `k` onwards?"
2. If `k == len(word)`, every letter is matched, so return `True`.
3. If the cell is outside the board, or its letter is not `word[k]` (a visited cell holds `"#"`, which never matches), return `False`.
4. Otherwise, save the letter and overwrite the cell with `"#"` so it cannot be reused.
5. Search the four neighbors for the next letter (`k + 1`) and combine them with `or`.
6. Restore the saved letter, then return the result.
7. Run `search(r, c, 0)` from every cell, and return `True` if any start succeeds.

# Complexity
- Time complexity: $$O(m \cdot n \cdot 3^L)$$, where `L` is the length of the word. Every cell can start a search, and after the first step each call has at most 3 new directions, since the cell it came from is marked.

- Space complexity: $$O(L)$$ for the recursion depth. The board is reused for the visited marks, so no extra grid is needed.

# Code

# --- CODE ---
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row = len(board)
        col  = len(board[0])

        def search (r, c, k):
            if(k == len(word)):
                return True
            if ( (r<0 or r>=row) or (c<0 or c>=col) ):
                return False
            if (board[r][c] != word[k]):
                return False 

            letter = board[r][c]
            board[r][c] = "#"    

            out= (search(r+1 , c, k+1) or search(r-1 , c, k+1) or search(r , c+1, k+1) or search(r , c-1, k+1))

            board[r][c]=letter

            return out 
        
        for r in range (row):
            for c in range (col):
                if(search(r,c,0)):
                    return True 
        return False

