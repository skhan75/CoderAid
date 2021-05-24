class TransitiveClosure {

	// Runtime --> O(n^3)
	static int[][] getTransitiveClosureUsingFloydWarshall(int[][] graph) {
		int m = graph.length;
		int reach[][] = new int[m][m];

		for(int i=0; i<m; i++){
			for(int j=0; j<m; j++){
				reach[i][j] = graph[i][j];
			}
		}

		for(int k=0; k<m; k++) {
			for(int i=0; i<m; i++) {
				for(int j=0; j<m; j++) {
					if(reach[i][j] != 0 || (reach[i][k]!=0 && reach[k][j]!=0)) {
						reach[i][j] = 1;
					} else{
						reach[i][j] = 0;
					}
				}
			}
		}
		return reach;
	}


	// Runtime --> O(n^2)
	static int[][] getTransitiveClosureUsingDFS(int[][] graph) {

		int m = graph.length;
		int reach[][] = new int[m][m];

		for(int i=0; i<m; i++) {
			for(int j=0; j<m; j++) {
				reach[i][j] = graph[i][j];
			}
		}

		for(int i=0; i<m; i++) {
			DFS(i,i, reach);
		}

		return reach;


	}

	static void DFS(int u, int v, int[][] reach) {

		reach[u][v] = 1;

		for(int k=0; k<reach.length; k++) {
			if(reach[u][k]==0){
				DFS(u,k,reach);
			}
		}
	}

	void printSolution(int reach[][]) {
        System.out.println("The following matrix shows the shortest "+
                         "distances between every pair of vertices");
        for (int i=0; i<reach.length; ++i) {
            for (int j=0; j<reach.length; ++j) {
                if (i==j)
                    System.out.print("1 ");
                else
                    System.out.print(reach[i][j]+" ");
            }
            System.out.println();
        }
    }

	public static void main(String[] args) {
		int graph[][] = new int[][]{
			{1, 1, 0, 1},
	    	{0, 1, 1, 0},
	      	{0, 0, 1, 1},
	     	{0, 0, 0, 1}
	    };

		TransitiveClosure transitiveClosure = new TransitiveClosure();
		int reach[][] = transitiveClosure.getTransitiveClosureUsingFloydWarshall(graph);

		transitiveClosure.printSolution(reach);

		int reach2[][] = transitiveClosure.getTransitiveClosureUsingDFS(graph);

		transitiveClosure.printSolution(reach2);

		



	}
}