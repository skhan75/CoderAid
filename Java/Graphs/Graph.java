import java.util.*;


public class Graph {
	int size = 0;
	int noOfEdges = 0;
	boolean isDirected = false;

	// Define a Map of Nodes and its ist of neighbors
	HashMap<Node, LinkedList<Node>> graphMap;

	public Graph() {
		// Initialize a Map for the Graph object
		graphMap = new HashMap<>();	
	}

	public Graph(boolean isDirected) {
		// Initialize a Map for the Graph object
		graphMap = new HashMap<>();	
		this.isDirected = isDirected;
	}

	public int noOfEdges() {
		return this.noOfEdges;
	}

	public boolean hasEdge(Node src, Node dest) {
		return this.graphMap.containsKey(src) && this.graphMap.get(src).contains(dest);
	}

	public Node pickFirstNode() {
		Iterator <Node> iterator = this.graphMap.keySet().iterator();
		if(iterator.hasNext()) {
			return iterator.next();
		}
		return null;
	}
 
	public void addEdgeHelpers(Node src, Node dest) {
		// Get the list of adjacent neighbors of source node 'u'
		LinkedList<Node> sourceNeighbors = this.graphMap.get(src);

		if(!sourceNeighbors.contains(dest)) {
			sourceNeighbors.add(dest);
			this.graphMap.put(src, sourceNeighbors);
		}
	}

	public void addEdge(Node src, Node dest) {
		if(!this.graphMap.keySet().contains(src)) {
			this.graphMap.put(src, new LinkedList<>());
		}

		if(!graphMap.keySet().contains(dest)) {
			this.graphMap.put(dest, new LinkedList<>());
		}

		this.addEdgeHelpers(src, dest);

		if(!this.isDirected) {
			this.addEdgeHelpers(dest, src);
		}

		this.noOfEdges++;
	}

	public void printEdges() {
        for (Node node : this.graphMap.keySet()) {
            System.out.print("Vertex " + node.name + " has an edge towards: ");
            if (!this.graphMap.get(node).isEmpty()) {
                for (Node neighbor : this.graphMap.get(node)) {
                    System.out.print(neighbor.name + " ");
                }
                System.out.println();
            }
            else {
                System.out.println("none");
            }
        }
    }

    static class Node {
		int key;
		String name;
		boolean visited;

		public Node(int key, String name) {
			this.key = key;
			this.name = name;
		}

		public Node(int key, String name, boolean visited) {
			this.key = key;
			this.name = name;
			this.visited = visited;
		}

		void visit() {
			this.visited = true;
		}

		void unvisit() {
			this.visited = false;
		}

		void setKey(int key) {
			this.key = key;
		}

		int getKey() {
			return this.key;
		}

		void setName(String name) {
			this.name = name;
		}

		String getName() {
			return this.name;
		}

		Boolean isVisited() {
			return this.visited;
		}
	}

	public void breadthFirstSearch(Node node) {

		if(node == null) return;

		LinkedList<Node> queue = new LinkedList<>();
		queue.add(node);
		// System.out.println("CUJRRE1 " + node.name);

		while(!queue.isEmpty()) {	

			// Pop the the current node from the queue
			Node currentNode = queue.removeFirst();

			// If current node is visited, we skip that node from traversal
			if(currentNode.isVisited()) continue;

			// Mark the current node as visited
			currentNode.visit();

			System.out.println(currentNode.name);

			// Get the neighbors of the current node
			LinkedList<Node> allNeighbors = this.graphMap.get(currentNode);

			if(allNeighbors.isEmpty()) continue;

			for(Node neighbor : allNeighbors) {
				if(!neighbor.isVisited()) {
					queue.add(neighbor);
				}
			}
		}

		System.out.println();
	}

	public void depthFirstSearch(Node node) {
		node.visit();

		System.out.println(node.name + " ");

		// Get all the neighbors of the current node
		LinkedList<Node> allNeighbors = this.graphMap.get(node);

		if(allNeighbors.isEmpty()) return;

		for(Node neighbor : allNeighbors) {
			// System.out.println("NE "+neighbor.name);
			if(!neighbor.isVisited()) {
				depthFirstSearch(neighbor);
			}
		}
	}

	public void resetNodesVisited(){
	    for(Node node : this.graphMap.keySet()){
	        node.unvisit();
	    }
	}


	public static void main(String[] args) {
		Graph graph = new Graph();

		// Create Graph Nodes
		Node a = new Node(0, "A", false);
		Node b = new Node(1, "B", false);
		Node c = new Node(2, "C", false);
		Node d = new Node(3, "D", false);
		Node e = new Node(4, "E", false);
		Node f = new Node(5, "F", false);

		graph.addEdge(a,b);
        graph.addEdge(b,c);
        graph.addEdge(b,d);
        graph.addEdge(c,e);
        graph.addEdge(b,a);

        graph.printEdges();

        System.out.println("Has Edge " + graph.hasEdge(a,b));
        System.out.println("Has Edge " + graph.hasEdge(a,e));
        System.out.println("Number of Edges " + graph.noOfEdges);

        System.out.println("BFS Traversal");
        graph.breadthFirstSearch(a);

        graph.resetNodesVisited();

		System.out.println("DFS Traversal");
        graph.depthFirstSearch(a);

	}

}

