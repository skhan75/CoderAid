/** Classic example of topological ordering **/
static int WHITE = 1;
static int GRAY = 2; // An edge to a gray vertex represents a cycle 
static int BLACK = 3;

boolean isPossible;
Map<Integer, List<Integer>> graph;
Map<Integer, Integer> color; // this will be used to mark the order of visits
List<Integer> topologicalOrder;

public int[] findOrder(int numCourses, int[][] prerequisites) {

	// Mark all the nodes as WHITE or unvisited
	init();

	// build graph
	buildGraph(prerequisites);

	for(int i=0; i<numCourses; i++) {
		if(this.color.get(i) == WHITE)
			this.dfs(i);
	}

	int[] order;
	if(this.isPossible) {
		order = new int[numCourses];
		for(int i=0; i<numCourses; i++)
			order[i] = this.topologicalOrder.get(i);
	} else {
		order = new int[0];
	}

	return order;
}

private void dfs(int node) {
	if(!this.isPossible)
		return;

	// start the recursion
	for(Integer nei : graph.getOrDefault(node, new ArrayList<>())) {
		if(this.color.get(nei) == WHITE) 
			this.dfs(nei);
		else if(this.color.get(nei) == GRAY) // Because an edge to a GRAY vertex represents a cycle, so this is not possible
			this.isPossible = false;
	}

	this.color.put(node, BLACK);
	this.topologicalOrder.add(node); // adding node in the topological ordering
}

private void buildGraph() {

	for(int[] relation : prerequisites) {
		int course = relation[0];
		int prereq = relation[1];

		List<Integer> prereqList = this.graph.getOrDefault(course, new LinkedList<>());
		prereqList.add(prereq);
		graph.put(course, prereqList);
	}
}	

private void init() {
	this.isPossible = true;
	this.color = new HashMap<>();
	this.graph = new HashMap<>();
	this.topologicalOrder = new ArrayList<>();

	for(int i=0; i<numCourses; i++)
		this.color.put(i, WHITE);
}