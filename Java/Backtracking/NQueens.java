import java.util.*;

class NQueens {
    private int size;
    private List<List<String>> result = new ArrayList<List<String>>();
    private static char QUEEN = 'Q';
    private static char EMPTY = '.';

    public List<List<String>> solveNQueens(int n) {

        this.size = n;
        char[][] chessboard = new char[n][n];

        // initialize the chess borad with empty spaces
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++)
                chessboard[r][c] = EMPTY;

        int row = 0;
        Set<Integer> diagonals = new HashSet<>();
        Set<Integer> antiDiagonals = new HashSet<>();
        Set<Integer> colsPlacements = new HashSet<>();

        backtrack(row, diagonals, antiDiagonals, colsPlacements, chessboard);

        return result;

    }

    private List<String> createSolution(char[][] chessboard) {

        List<String> board = new ArrayList<>();
        for (int row = 0; row < this.size; row++) {
            String currentRow = new String(chessboard[row]); // convert all the row chars in one string
            board.add(currentRow);
        }

        return board;
    }

    private void backtrack(int row, Set<Integer> diagonals, Set<Integer> antiDiagonals, Set<Integer> colsPlacements,
            char[][] chessboard) {

        // Base case
        if (row == this.size) {
            result.add(createSolution(chessboard));
            return;
        }

        // choice
        for (int col = 0; col < size; col++) {
            int currDiagonalKey = row - col; // Diagonals that lie in the same row-col
            int currAntidiagonalKey = row + col; // Antidiagonals that lie int same row+col

            // if queen is not placeable then continue
            if (colsPlacements.contains(col) || diagonals.contains(currDiagonalKey)
                    || antiDiagonals.contains(currAntidiagonalKey))
                continue;

            // DO - Else add the queen to the board
            colsPlacements.add(col);
            diagonals.add(currDiagonalKey);
            antiDiagonals.add(currAntidiagonalKey);
            chessboard[row][col] = QUEEN;

            // BACKTRACK - Move on to the next row with the updated chessboard and check for
            // other placemenets
            backtrack(row + 1, diagonals, antiDiagonals, colsPlacements, chessboard);

            // UNDO - Remove the current placement of the Queen and check for other valid
            // placemnents
            colsPlacements.remove(col);
            diagonals.remove(currDiagonalKey);
            antiDiagonals.remove(currAntidiagonalKey);
            chessboard[row][col] = EMPTY;
        }
    }
}
