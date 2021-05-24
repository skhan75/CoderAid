import java.util.*;

class MotherVertex {

	void addEdge(int u, int v, ArrayList<ArrayList<Integer>> adj){
		adj.get(u).add(v);
	} 

	void DFS(ArrayList<ArrayList<Integer>> g, int v, boolean[] visited) {
		visited[v] = true;
		for(int x: g.get(v)) {
			if(!visited[x]) {
				DFS(g, x, visited);
			}
		}
	}

	int findMotherVertex(ArrayList<ArrayList<Integer>> graph, int V) {
		boolean[] visited = new boolean[V];

		int v = -1;

		for(int i=0; i<V; i++){
			if(!visited[i]) {
				DFS(graph, i, visited);
				v = i;
			}
		}

		boolean[] check = new boolean[V];
		DFS(graph, v, check);
		for(boolean val : check){
			if(!val){
				return -1;
			}
		}

		return v;
	}

	public static void main(String[] args) {
		int V = 7;
		int E = 8;

		ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>();


		// Initialize empty list for each node
		for(int i=0; i<V; i++){
			adj.add(new ArrayList<Integer>());
		}

		MotherVertex mv = new MotherVertex();

		mv.addEdge(0, 1,adj);
	    mv.addEdge(0, 2,adj);
	    mv.addEdge(1, 3,adj);
	    mv.addEdge(4, 1,adj);
	    mv.addEdge(6, 4,adj);
	    mv.addEdge(5, 6,adj);
	    mv.addEdge(5, 2,adj);
	    mv.addEdge(6, 0,adj);
	     
	    System.out.println("The mother vertex is " +
	                        mv.findMotherVertex(adj, V));
	}

}

