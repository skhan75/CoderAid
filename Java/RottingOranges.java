int rows, cols;
int[][] ans;

public int orangesRotting(int[][] grid){

	rows = grid.length;
	cols = grid[0].length;

	ans = new int[rows][cols];
	for(int i=0; i<rows; i++) {
		for(int j=0; j<cols; j++) {
			ans[i][j] = Integer.MAX_VALUE;
		}
	}

	for(int i=0; i<rows; i++) {
		for(int j=0; j<cols; j++) {
			if(grid[i][j] == 2)
				rotTheOranges(grid, i, j, 0);
		}
	}

	// Get the answer
	int res = 0;
	for(int i=0; i<rows; i++) {
		for(int j=0; j<cols; j++) {
			if(grid[i][j] == 1)
				res = Math.max(res, ans[i][j])
		}
	}

	return res == Integer.MAX_VALUE ? -1 : res;
}

private void rotTheOranges(int[][] grid, int r, int c, int time) {

	// Set the boundary
	if(r<0 || c<0 || r>=rows || c>=cols || grid[r][c] == 0)
		return;

	// check if we have not already visited this orange and rotten it in a better time
	if(ans[r][c] <= time)
		return;
	
	// if we encounter an already rotten orange while its not the first rotten orange
	if(time!=0 && grid[r][c] == 2)
		return;

	ans[r][c] = time;

	rotTheOranges(grid, r+1, c, time+1);
	rotTheOranges(grid, r-1, c, time+1);
	rotTheOranges(grid, r, c+1, time+1);
	rotTheOranges(grid, r, c-1, time+1);
}