# ============================================================
#  Problem : Set Matrix Zeroes
#  URL     : https://leetcode.com/problems/set-matrix-zeroes/
#  Solution: https://leetcode.com/solutions/set-matrix-zeroes-leetcode-73-by-sanskar-dmki/
#  Date    : 2026-11-07
#  Author  : Sanskar_phougat
# ============================================================

# --- WRITE-UP ---
# Set Matrix Zeroes | LeetCode 73

## Intuition

The main challenge is to set the entire row and column to zero whenever an element is zero, without losing information about the original positions of zeroes.

Instead of using additional arrays or sets to store the zero positions, we can use the **first row and first column of the matrix itself as markers**.

Since the first cell (`matrix[0][0]`) belongs to both the first row and first column, we maintain two separate Boolean flags to track whether the first row and first column originally contained a zero.

## Approach

1. First, check whether the first row contains any zero and store the result in a Boolean variable.
2. Similarly, check whether the first column contains any zero.
3. Traverse the remaining matrix, excluding the first row and first column.
4. Whenever a zero is encountered at position `(i, j)`:
   - Mark its corresponding row by setting `matrix[i][0] = 0`.
   - Mark its corresponding column by setting `matrix[0][j] = 0`.
5. Traverse the matrix again and use these markers to set the required rows and columns to zero.
6. Finally, use the two Boolean flags to handle the first row and first column separately.

The important idea is to complete the marking process before modifying the corresponding rows and columns. This prevents newly created zeroes from being treated as original zeroes.

## Complexity

- **Time Complexity:** O(m × n), where m is the number of rows and n is the number of columns. We traverse the matrix a constant number of times.
- **Space Complexity:** O(1), since we use the matrix itself for marking and only maintain two Boolean variables.

# Code

# --- CODE ---
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:

        if not matrix:
            return

        row = len(matrix)
        col = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Step 1: Check whether first row contains zero
        for j in range(col):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Step 2: Check whether first column contains zero
        for i in range(row):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Step 3: Mark zeros using first row and column
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 4: Set corresponding rows to zero
        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(1, col):
                    matrix[i][j] = 0

        # Step 5: Set corresponding columns to zero
        for j in range(1, col):
            if matrix[0][j] == 0:
                for i in range(1, row):
                    matrix[i][j] = 0

        # Step 6: Handle first row
        if first_row_zero:
            for j in range(col):
                matrix[0][j] = 0

        # Step 7: Handle first column
        if first_col_zero:
            for i in range(row):
                matrix[i][0] = 0

