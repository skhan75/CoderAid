import java.util.*;

class KCores {

	static class Graph {

		int V;
		HashMap<Integer, LinkedList<Integer>> graphMap;

		Graph(int V) {
			this.V = V;
			this.graphMap = new HashMap<>();

			for(int i=0; i<V; i++){
				this.graphMap.put(i, new LinkedList<Integer>());
			}
		}

		void addEdgeHelper(int u, int v) {
			LinkedList<Integer> sourceNeighbors = this.graphMap.get(u);

			if(!sourceNeighbors.contains(v)) {
				sourceNeighbors.add(v);
				this.graphMap.put(u, sourceNeighbors);
			}
		}

		void addEdge(int u, int v) {		
			addEdgeHelper(u, v);
			addEdgeHelper(v, u);
		}
	}

	void printKCores(int k, Graph g) {
		// Mark all the vertices as not visited and not processed
		boolean[] visited = new boolean[g.V];
		boolean[] processed = new boolean[g.V];

		Arrays.fill(visited, false);
		Arrays.fill(processed, false);

		// Store all the degrees of the vertex
		int[] vDegree = new int[g.V];
		for(int i=0; i<g.V; i++) {
			vDegree[i] = g.graphMap.get(i).size();
		}

		// DFS traversal to update degrees of all the vertices
		for(int i=0; i<g.V; i++) {
			if(visited[i] == false) {
				this.DFS(i, visited, vDegree, k, g);
			}	
		}

	  // PRINTING K CORES
        System.out.println("K-Cores : "+ k);
        for (int v=0; v<g.V; v++) {

            // Only considering those vertices which have degree
            // >= K after BFS
            if (vDegree[v] >= k) {
                System.out.printf("\n[%d]", v);

                // Traverse adjacency list of v and print only
                // those adjacent which have vDegree >= k after
                // BFS.
                for (int i : g.graphMap.get(v))
                    if (vDegree[i] >= k)
                        System.out.printf(" -> %d", i);
            }
        }
	}

	void DFS(int v, boolean[] visited, int[] vDegree, int k, Graph g) {
		// Mark the current node as visited
		visited[v] = true;

		// Recur for all th vertices adjacent to this vertex
		for(int i: g.graphMap.get(v)) {
			// if degree of v is less than k, then its adjacent neighbor's degree should be reduced too
			if(vDegree[v]<k){
				vDegree[i]--;
			}

			// if adjacent neighbor has not been visited yet, process it
			if(!visited[i]){
				DFS(i, visited, vDegree, k, g);
			}
		}

	}

	public static void main(String[] args) {

		Graph g1 = new Graph(9);
		g1.addEdge(0, 1);
        g1.addEdge(0, 2);
        g1.addEdge(1, 2);
        g1.addEdge(1, 5);
        g1.addEdge(2, 3);
        g1.addEdge(2, 4);
        g1.addEdge(2, 5);
        g1.addEdge(2, 6);
        g1.addEdge(3, 4);
        g1.addEdge(3, 6);
        g1.addEdge(3, 7);
        g1.addEdge(4, 6);
        g1.addEdge(4, 7);
        g1.addEdge(5, 6);
        g1.addEdge(5, 8);
        g1.addEdge(6, 7);
        g1.addEdge(6, 8);

        KCores kCores = new KCores();

		kCores.printKCores(3, g1);

	}
}