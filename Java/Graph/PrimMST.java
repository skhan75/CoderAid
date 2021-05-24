import java.util.*;

public class PrimMST {

	public List<Edge<Integer>> primMST(Graph<Integer> graph) {
		
		// Initializae a Binary Min Heap (PriorityQueue) Data structure
		BinaryMinHeap<Vertex<Integer>> minHeap = new BinaryMinHeap<>();

		// Map of vertex to edge which gave minimum weight to this vertex 
		Map<Vertex<Integer>, Edge<Integer>> vertexToEdge = new HashMap<>();

		// Stores the final result
		List<Edge<Integer>> result = new ArrayList<>();

		// Initialize all the vertices with infinite weights
		for(Vertex<Integer> v : graph.getAllVertices()) {
			minHeap.add(Integer.MAX_VALUE, v);
		}

		// Start from any random vertex
		Vertex<Integer> startVertex = graph.getAllVertices().iterator().next();

		// For the start vertex, we decrease the value in min heap to 0, as start vertex cost to itself is 0
		minHeap.decrease(startVertex, 0);

		// Iterate till min heap has elements in it
		while(!minHeap.empty()) {
			// Extract min cost vertex from the min heap
			Vertex<Integer> current = minHeap.extractMin();

			// Get the corresponding edge contributing to the minimum cost edge from the current
			Edge<Integer> spanningTreeEdge = vertexToEdge.get(current);
			if(spanningTreeEdge!=null) {
				result.add(spanningTreeEdge);
			}

			// iterate through all the adjacent vertices
			for(Edge<Integer> edge : current.getEdges()) {
				Vertex<Integer> adjacentVertex = getVertexForEdge(current, edge);
				// Check if adjacent vertex exists in min heap and cost attached with this vertex is greater than this edge weight
				if(minHeap.containsData(adjacentVertex) && minHeap.getWeight(adjacentVertex) > edge.getWeight()) {
					// Adjust the weight the adjacent vertex to this edge's weight
					minHeap.decrease(adjacentVertex, edge.getWeight());

					// add vertex-->edge mapping the graph
					vertexToEdge.put(adjacentVertex, edge);
				}
			}
		}
		return result;

	}

	private Vertex<Integer> getVertexForEdge(Vertex<Integer> v, Edge<Integer> e){
        return e.getUvertex().equals(v) ? e.getVvertex() : e.getUvertex();
    }



	public static void main(String[] args) {

		Graph<Integer> graph = new Graph<>(false);
		graph.addEdge(1, 2, 3);
        graph.addEdge(2, 3, 1);
        graph.addEdge(3, 1, 1);
        graph.addEdge(1, 4, 1);
        graph.addEdge(2, 4, 3);
        graph.addEdge(4, 5, 6);
        graph.addEdge(5, 6, 2);
        graph.addEdge(3, 5, 5);
        graph.addEdge(3, 6, 4);

        PrimMST pmst = new PrimMST();

        Collection<Edge<Integer>> edges = pmst.primMST(graph);
		for(Edge<Integer> edge : edges){
            System.out.println(edge);
        }
	}
}