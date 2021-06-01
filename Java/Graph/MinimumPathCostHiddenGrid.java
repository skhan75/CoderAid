

class MinimumCostPathHiddenGrid {
	class Pair {
		int row, col;

		Pair(int row, int col) {
			this.row = row;
			this.col = col;
		}
	}

	public int findShortestPath(GridMaster master) {


		Map<Char, Pair> directions = new HashMap<Char, Pair>();
		directions.put('U', new Pair(-1,0));
		directions.put('D', new Pair(1,0));
		directions.put('L', new Pair(0,-1));
		directions.put('R', new Pair(0,1));



		Pair targetPair = new Pair(150, 150);
		int[][] grid = new int[]

		// Construct Grid with the given information

		// Create the Grid using DFS
		DFS(master, grid, 150, 150, directions, /*cost=*/1, start);

	}

	void DFS(GridMaster grid, int row, int col, char[] directions, int cost, Pair targetPair) {


		// If current cell is the target cell, then we mark the target cell
		if(master.isTarget()) {
			targetPair.row = row;
			targetPair.col = col;
		}

		for(Map.Entry<Char, Pair> dir : directions) {
			int newRow = row + dir.
		}

	}
}