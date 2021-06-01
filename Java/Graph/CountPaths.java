import java.util.*;

public class CountPaths {

	private int size;
	private LinkedList<Integer> adj[];
	int pathCount = 0;

	@SuppressWarnings("unchecked")
	CountPaths(int size) {
		this.size = size;
		adj = new LinkedList[this.size];
		for(int i=0; i<this.size; i++) {
			adj[i] = new LinkedList<>();
		}
	}

	void addEdge(int u, int v) {
		adj[u].add(v);
	}
	

	void countPathsUtil(int src, int dest, boolean[] visited) {
		if(src == dest) {
			pathCount++;
			return;
		}

		if(visited[src] == true){
			return;
		}

		Iterator<Integer> i = adj[src].listIterator();
		while(i.hasNext()) {
			int n = i.next();
			if(visited[n] == false) {
				countPathsUtil(n, dest, visited);
			}
		}

		// Mark the current vertex as unvisited
		visited[src] = false;

		return;

	}

	int countPaths(int src, int dest) {
		boolean[] visited = new boolean[size];
		Arrays.fill(visited, false);
		
		countPathsUtil(src, dest, visited);

		return pathCount;
	}

	public static void main(String[] args) {
		CountPaths g = new CountPaths(5);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(0, 3);
        g.addEdge(1, 3);
        g.addEdge(2, 3);
        g.addEdge(1, 4);
        g.addEdge(2, 4);
 
        int s = 0, d = 3;

        System.out.println(g.countPaths(s, d));

	}
}