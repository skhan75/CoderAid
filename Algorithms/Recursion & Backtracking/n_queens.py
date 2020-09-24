"""
The n-queens puzzle is the problem of placing n queens
on an nxn chessboard such that no two queens attack each other.



- All the cells in the same row, as the current placed Queen will be under attack
- All the cells in the same col, as the current placed Queen will be under attack
- There are two diaganols from the current place cell, topLeft-bottomRight diagonal and bottomLeft-topRight diagonal:
    - The diagnoals having same difference will be under attack
    - So, cells in the same topLeft-bottomeRight diagonal will be calculated as (row-col)
    - And cells in the same bottomLeft-topRight diagonal will be calculated as (row+col)
"""


class Solution(object):
    def totalNQueens(self, n):

        def is_not_under_attack(row, col):
            return not (rows[col] or topLeft_bottomRight_diagonal[row-col] or bottomLeft_topRight_diagonal[row+col])

        def place_queen(row, col):
            # Every row can have only 1 queen (so 1 row per col)
            # Place queen on the current cell
            rows[col] = 1
            topLeft_bottomRight_diagonal[row-col] = 1
            bottomLeft_topRight_diagonal[row+col] = 1

        def remove_queen(row, col):
            rows[col] = 0
            topLeft_bottomRight_diagonal[row-col] = 0
            bottomLeft_topRight_diagonal[row+col] = 0

        def backtrack(row, count=0):
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    # When reached the end of board
                    if row + 1 == n:
                        count += 1
                    # Else check for more cells
                    else:
                        count = backtrack(row+1, count)
                    # Remove queen and check other possibilities
                    remove_queen(row, col)

            return count

        rows = [0] * n
        topLeft_bottomRight_diagonal = [0] * (2 * n - 1)
        bottomLeft_topRight_diagonal = [0] * (2 * n - 1)

        return backtrack(0,0)


s = Solution()
print s.totalNQueens(4)
print s.totalNQueens(5)
