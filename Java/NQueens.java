
private int size;
private static QUEEN = 'Q';
private static EMPTY = '.';
private List<List<String>> solution;

public List<List<String>> solveNQueens(int n) {

	this.size = n;

	// create a chessboard of characters representing Queen and Empty Spaces
	char[][] chessboard = new int[n][n];

	// initialize chessboard with empty spaces
	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
			chessboard[i][j] = this.EMPTY;

	// We start from row 0
	int row = 0;
	Set<Integer> diagonals = new HashSet<>();
	Set<Integer> antidiagonals = new HashSet<>();
	Set<Integer> colsPlacements = new HashSet<>();
	backtrack(row, diagonals, antidiagonals, colsPlacements, chessboard);

	return result;
}

private void backtrack(int row, Set<Integer> diagonals, Set<Integer> antiDiagonals, Set<Integer> colsPlacements, char[][] chessboard) {

	// base case
	// if we are able to reach the size, that means then we had our valid placements
	if(row == this.size){
		result.add(createSolution(chessboard));
		return;
	}

	// choice
	// Check every cols
	for(int col=0; col<this.size; col++) {
		int currDiagonalKey = row - col;
		int currAntidiagonalKey = row + key;

		// If queen is not placeable we continue
		if(colsPlacements.contains(col) || diagonals.contains(currDiagonalKey) || antidiagonals.contains(antidiagonals))
			continue;

		// Else add the Queen to the chessboard
		colsPlacements.add(col);
		diagonals.add(currDiagonalKey);
		antidiagonals.add(currAntidiagonalKey);
		chessboard[row][col] = this.QUEEN;

		// Backtrack
		backtrack(row+1, diagonals, antidiagonals, colsPlacements. chessboard);

		// Undo the choice to consider other possibilities
		colsPlacements.remove(col);
		diagonals.remove(currDiagonalKey);
		antidiagonals.remove(currAntidiagonalKey);
		chessboard[row][col] = this.EMPTY;
	}
}