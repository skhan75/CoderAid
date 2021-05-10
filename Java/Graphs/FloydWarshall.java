class FloydWarshall {
	final static int INF = 99999;
	int V = 4;

	void getAllShortestPairPath(int[][] graph) {

		int solution[][] = new int[V][V];

		for(int i=0; i<V; i++){
			for(int j=0; j<V; j++){
				solution[i][j] = graph[i][j];
			}
		}

		for(int k=0; k<V; k++){
			for(int i=0; i<V; i++){
				for(int j=0; j<V; j++){
					solution[i][j] = Math.min(solution[i][j], solution[i][k] + solution[k][j]);
				}
			}
		}

		this.printSolution(solution);

	}

	void printSolution(int dist[][]) {
        System.out.println("The following matrix shows the shortest "+
                         "distances between every pair of vertices");
        for (int i=0; i<V; ++i) {
            for (int j=0; j<V; ++j) {
                if (dist[i][j]==INF)
                    System.out.print("INF ");
                else
                    System.out.print(dist[i][j]+"   ");
            }
            System.out.println();
        }
    }


	public static void main(String[] args) {
		int graph[][] = { {0, 3,   INF, 7  },
                          {8, 0,   2,   INF},
                          {5, INF, 0,   1  },
                          {2, INF, INF, 0  }
                        };
		FloydWarshall floydWarshall = new FloydWarshall();
		floydWarshall.getAllShortestPairPath(graph);
	}
}