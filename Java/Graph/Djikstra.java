import java.util.*;

class Dijkstra {

	public Map<Vertex<Integer>, Integer> shortestPath(Graph<Integer> graph, Vertex<Integer> sourceVertex) {

		// Min Heap to store vertices with cost
		BinaryMinHeap<Vertex<Integer>> minHeap = new BinaryMinHeap<>();

		// Distance Map from Source to all other vertices in the graph
		Map<Vertex<Integer>, Integer> distanceMap = new HashMap<>();

		// Parent Map to map which vertex is coming from which parent
		Map<Vertex<Integer>, Vertex<Integer>> parent = new HashMap<>();


		/**
			1. Create a minHeap with all vertices with their cost as INF
			2. Mark cost of source vertex as 0, and extract it from minHeap
			3. Put the vertex in distanceMap, with their distance (cost)
			2. Extract adjacent vertex of sourceVertex from minHeap with minimum cost
			3. 
		**/

		for(Vertex<Integer> vertex : graph.getAllVertices()) {
			minHeap.add(Integer.MAX_VALUE, vertex);
		}

		// Decrease the cost of current/source vertex as 0, as cost to itself is 0
		minHeap.decrease(sourceVertex, 0);

		// Put this in the distanceMap
		distanceMap.put(sourceVertex, 0);

		// Put the parent of source vertex as null
		parent.put(sourceVertex, null);

		// Iterate till heap is not empty
		while(!minHeap.isEmpty()) {
			// Extract the vertex with minimum cost, which has vertex and distance of that vertex from source vertex
			BinaryMinHeap<Vertex<Integer>>.Node minNode = minHeap.extractMinNode();

			Vertex<Integer> current = minNode.key;

			// update the shortest distance of current from the source vertex
			distanceMap.put(current, minNode.weight);

			// explore the neighbors of current vertex
			for(Edge<Integer> edge : current.getEdges()) {

				// Get the adjacent vertex from the edge
				Vertex<Integer> adjacentVertex = getVertexForEdge(current, edge);

				// If heap does not contain any adjacent vertex, that means vertex already has shortest distance from the source vertex
				if(!minHeap.containsData(adjacentVertex)) {
					continue;
				}


				// Add distance of current vertex weight to the adjacent vertex from source vertex
				int newDistance = distanceMap.get(current) + edge.getWeight();

				// If this total distance is less than current stored distance, then decrease the weight 
				if(minHeap.getWeight(adjacentVertex) > newDistance) {
					minHeap.decrease(adjacentVertex, newDistance);
					parent.put(adjacentVertex, current);
				}
			}
		}

		return distanceMap;
	}

	private Vertex<Integer> getVertexForEdge(Vertex<Integer> v, Edge<Integer> e) {
		return e.getUvertex().equals(v) ? e.getVvertex() : e.getUvertex();
	}

	public static void main(String[] args ){
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

        Dijkstra dsp = new Dijkstra();
        Vertex<Integer> sourceVertex = graph.getVertex(1);

        Map<Vertex<Integer>, Integer> distance = dsp.shortestPath(graph, sourceVertex);
        System.out.println(distance);
	}
}