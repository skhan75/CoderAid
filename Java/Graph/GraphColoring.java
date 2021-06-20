// Given a set of nodes, find the mininmum number of colors set such that all nodes are colored 
// with no adjacent node sharing the same color

import java.util.*;
import java.util.LinkedList;
import java.io.*;

class GraphColoring {
	int size;
	LinkedList<Integer> graph[]; // Adjacency List
	int[] colors;

	GraphColoring(int n) {
		this.size = n;
		graph = new LinkedList[n];
		for(int i=0; i<n; i++) {
			graph[i] = new LinkedList();
		}
	}

	public void addEdge(int u, int v) {
		graph[u].add(v);
		graph[v].add(u); // undirected graph
	}

	// Always go to a lower numbered color whenever we color a node
	public void greedyColoring() {
		int result[] = new int[this.size+1];
		Arrays.fill(result, -1);

		result[0] = 0;

		// An array to store the available colors at a given coloring sequence.
		boolean available[] = new boolean[this.size+1];
		Arrays.fill(available, false);

		// Assign color to remaining V-1 vertices
		for(int u=1; u<this.size; u++){
			// Assign colors to all adjacent neighbors
			Iterator<Integer> neighbor = graph[u].iterator();
			while(neighbor.hasNext()) {
				int i = neighbor.next();	
				// If the node is already colored, we mark the color corresponding to that node as not available
				if(result[i] != -1){
					available[result[i]] = false;
				}
			}

			// Find the first available color
			int col;
			for(col=0; col<this.size; col++){
				if(available[col]) {
					break;
				}
			}

			result[u] = col;

			Arrays.fill(available, true);
		}

		for(int i=0; i<this.size; i++) {
			System.out.println("Vertex " + i + " --->  Color " + result[i]);
		}
	}
	

	public boolean isMColorable(int m) {
		if(m == this.size) {
			return true;
		}

		// Create a color matrix for each vertex
		int color[] = new int[this.size];
		for(int i=0; i<this.size; i++) {
			color[i] = 0; // Initially set all the colors to 0
		}

		int startVertex = 0;
		return graphColoringUtil(m, color, startVertex);
	}

	public boolean graphColoringUtil(int m, int[] color, int node) {

		// If we are able to reach the last node, that means we were able to color all the nodes sucessfully
		if(node == this.size) {
			return true;
		}

		// for all colors from available colors, check if its a valid color to mark all the adjacent neighbors with m colors
		for(int curCol=1; curCol<=m; curCol++) {
			// Check if current color is a valid color for coloring current adjacent vertex
			if(isValid(node, color, curCol)) {
				color[node] = curCol;
				// Now you try keeping the current node with current color, the combinations which color all the vertices with m color
				// and once you find that combination, you just return true
				if(graphColoringUtil(m, color, node+1)){
					return true; // dont have to iterate more once found
				}
			}

			// When not found, that means current color-node pair didn't work out to give result
			// So we reset the current color-node combination
			color[node] = 0; 

		}

		return false;
	}

	public boolean isValid(int node, int[] color, int col) {
		// Check all the neighbors of current node to verify that none of the nodes have same color
		LinkedList<Integer> neighbors = graph[node];

		for(int neighbor : neighbors) {
			if(color[neighbor] == col) {
				return false;
			}
		}

		return true;
	}

	public static void main(String[] args) {
		GraphColoring g = new GraphColoring(5);
		g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 3);
        g.addEdge(3, 4);
        System.out.println("Coloring of graph 1");
        g.greedyColoring();

        System.out.println("Is colorable with 3 colors? " + g.isMColorable(3));
        System.out.println("Is colorable with 2 colors? " + g.isMColorable(2));
        // int[] colors = {0,0,0,0};




	}
}