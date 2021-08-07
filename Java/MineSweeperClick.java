import java.util.*;
class MineSweeperClick {

	int[][] minesweeperClick(boolean[][] field, int x, int y) {
	    int m = field.length;
	    int n = field[0].length;
	    
	    System.out.println(x + " " + y);
	    int[][] result = new int[m][n];
	    boolean[][] visited = new boolean[m][n];
	    
	    for(int i=0; i<m; i++) {
	        for(int j=0; j<n; j++){
	            result[i][j] = -1;
	            visited[i][j] = false;
	        }
	    }
	    
	    if(x>=m || x<0 || y>=n || y<0) {
	        return result;
	    }

	    if(visited[x][y] == true) {
	    	return result;
	    }

	    visited[x][y] = true;
	    
	    int currentCount = 0;
	    
	    if(x > 0 && x < m) {
	    	// check top
	    	if(field[x-1][y] == true) {
		        currentCount += 1;
		    }
	    }  
	    if(y >= 0 && y < n) {
	    	// check right 
	    	if(field[x][y+1] == true) {
		        currentCount += 1;
		    }
	    }
	    if(x >= 0 && x < m-1){
	    	// check bottom 
	    	if(field[x+1][y] == true) {
		        currentCount += 1;
		    } 
	    }
	    if(y == n) {
	    	// check left only
	    	if(field[x][y-1] == true) {
		        currentCount += 1;
		    }
	    }
	    if(y > 0 && x < m-1){
	    	// check bottomLeft only
		    if(field[x+1][y-1] == true) {
		        currentCount += 1;
		    } 
	    }
	    if(x < m-1 && y < n-1) {
	    	// check bottomRight only
	    	if(field[x+1][y+1] == true) {
		        currentCount += 1;
		    }
	    }
	    if(y > 0 && x > 0) {
	    	// check top left
	    	if(field[x-1][y-1] == true) {
		        currentCount += 1;
		    }
	    } 
	    if(x > 0 || y < n-1 ) {
	    	// check topRight
		    if(field[x-1][y+1] == true) {
		        currentCount += 1;
		    }
	    }
	    
	    
	    result[x][y] = currentCount;
	    
	    
	    if(currentCount == 0) {
	        // check left
	        minesweeperClick(field, x, y-1);
	        // check topLeft
	        minesweeperClick(field, x-1, y-1);
	        // check top
	        minesweeperClick(field, x-1, y);
	        // check topRight
	        minesweeperClick(field, x-1, y+1);
	        // check right
	        minesweeperClick(field, x, y+1);
	        // check bottomLeft
	        minesweeperClick(field, x+1, y-1);
	        // check bottom
	        minesweeperClick(field, x+1, y);
	        // check bottomRight
	        minesweeperClick(field, x+1, y+1);
	    }
   
    	return result;
	}


	public static void main(String[] args) {
		MineSweeperClick mc = new MineSweeperClick();
		boolean[][] fields = {
			{true,  false, true,  true,  false},
			{true,  false, false, false, false},
			{false, false, false, false, false},
			{true,  false, false, false, false}
		};


		int[][] res = mc.minesweeperClick(fields, 3, 2);
		for(int i=0; i<res.length; i++) {
			for(int j=0; j<res[0].length; j++) {
				System.out.print(res[i][j] + " ");
			}
			System.out.println();
		}
	}

}