import java.util.*;

public class Graph<T> {
	// allEdges is a list of all edges in the graph of type Edge<T>
	private List<Edge<T>> allEdges;
	// allVertices is a Map of all vertices in the Graph mapped with their unique vertex id
	private Map<Long, Vertex<T>> allVertices;
	boolean isDirected = false;

	public Graph(boolean isDirected) {
		allEdges = new ArrayList<Edge<T>>();
		allVertices = new HashMap<Long, Vertex<T>>();
		this.isDirected = isDirected;
	}

	public void addEdge(long id1, long id2) {
		addEdge(id1, id2, 0);
	}

	public void addVertex(Vertex<T> vertex) {
		if(allVertices.containsKey(vertex.getId())) {
			return;
		}
		allVertices.put(vertex.getId(), vertex);
		for(Edge<T> edge : vertex.getEdges()) {
			allEdges.add(edge);
		}
	}

	public Vertex<T> addSingleVertex(long id) {
		if(allVertices.containsKey(id)) {
			return allVertices.get(id);
		}
		Vertex<T> v = new Vertex<T>(id);
		allVertices.put(id, v);
		return v;
	}

	public Vertex<T> getVertex(long id){
        return allVertices.get(id);
    }

    public void addEdge(long id1, long id2, int weight) {
    	Vertex<T> u = null;
    	if(allVertices.containsKey(id1)) {
    		u = allVertices.get(id1);
    	} else {
    		u = new Vertex<T>(id1);
    		allVertices.put(id1, u);
    	}

    	Vertex<T> v = null;
    	if(allVertices.containsKey(id2)) {
    		v = allVertices.get(id2);
    	} else {
    		v = new Vertex<T>(id2);
    		allVertices.put(id2, v);
    	}

    	Edge<T> edge = new Edge<T>(u, v, isDirected, weight);
    	allEdges.add(edge);
    	u.addAdjacentVertex(edge, v);
    	if(!isDirected) {
    		v.addAdjacentVertex(edge, u);
    	}
    }

    public List<Edge<T>> getEdges() {
    	return allEdges;
    }

    public Collection<Vertex<T>> getAllVertices() {
    	return allVertices.values();
    }

    public void setDataForVertex(long id, T data) {
    	if(allVertices.containsKey(id)) {
    		Vertex<T> vertex = allVertices.get(id);
    		vertex.setData(data);
    	}
    }

    public static void main(String[] args) {
    	Graph graph = new Graph(false);

    	graph.addEdge(1, 2, 5);
        graph.addEdge(2, 3, 2);
        graph.addEdge(1, 4, 9);
        graph.addEdge(1, 5, 3);
        graph.addEdge(5, 6, 2);
        graph.addEdge(6, 4, 2);
        graph.addEdge(3, 4, 3);
    }

}

class Vertex<T> {
	long id;
	private T data;
	private List<Edge<T>> edges = new ArrayList<>();
	private List<Vertex<T>> adjacentVertices = new ArrayList<>();

	Vertex(long id) {
		this.id = id;
	}

	public long getId() {
		return id;
	}

	public void setData(T data) {
		this.data = data;
	}

	public T getData() {
		return data;
	}

	public List<Vertex<T>> getAdjacentVertices() {
		return adjacentVertices;
	}

	public List<Edge<T>> getEdges() {
		return edges;
	}

	public int getDegree() {
		return edges.size();
	}

	public void addAdjacentVertex(Edge<T> e, Vertex<T> v) {
		edges.add(e);
		adjacentVertices.add(v);
	}

	public String toString() {
		return String.valueOf(id);
	}
}


class Edge<T> {
	private boolean isDirected = false;
	private Vertex<T> uVertex;
	private Vertex<T> vVertex;
	private int weight;

	Edge(Vertex<T> uVertex, Vertex<T> vVertex) {
		this.uVertex = uVertex;
		this.vVertex = vVertex;
	}

	Edge(Vertex<T> uVertex, Vertex<T> vVertex, boolean isDirected, int weight) {
		this.uVertex = uVertex;
		this.vVertex = vVertex;
		this.weight = weight;
		this.isDirected = isDirected;
	}

	Edge(Vertex<T> uVertex, Vertex<T> vVertex, boolean isDirected) {
		this.uVertex = uVertex;
		this.vVertex = vVertex;
		this.isDirected = isDirected;
	}

	Vertex<T> getUvertex() {
		return uVertex;
	}

	Vertex<T> getVvertex() {
		return vVertex;
	}

	int getWeight() {
		return weight;
	}

	public boolean isDirected() {
		return isDirected;
	}

	@Override
	public String toString() {
		return "Edge [isDirected = " + isDirected + ", uVertex = " + uVertex + ", vVertex = "+ vVertex + " weight = " + weight + "]";
	}
}