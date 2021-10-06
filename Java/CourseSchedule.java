
Map<Integer, List<Integer>> graph;
public boolean canFinish(int numCourses, int[][] prerequisites) {

	// Build Graph
	buildGraph(prerequisites);

	boolean[] visited = new boolean[numCourses];
	boolean[] checked = new boolean[numCourses];

	for(int i=0; i<numCourses; i++) }{
		if(isCyclic(i, visited))
			return false;
	}

	return true;
}

private boolean isCyclic(int course, boolean[] visited) {

	// Memoization 
	if(checked[course])
		return false;

	if(visited[course]) // cyclic
		return true;

	if(!graph.containsKey(course)) // no graph relation, that means independent course
		return false;

	visited[course] = true;

	boolean ret;
	for(int child : graph.get(course)) {
		ret = isCyclic(child, checked, visited);
		if(ret)
			break;
	}

	// after all the child has been visited and one whole backtracking is completed succesfully
	// remove the node from the path
	visited[course] = false;
	checked[course] = true;

	return ret;
}


private void buildGraph(int[][] prerequisites) {
	graph = new HashMap<>();

	for(int[] relation : prerequisites) {
		int course = relation[0];
		int prereq = relation[1];

		List<Integer> prereqList = graph.getOrDefault(course, new ArrayList<>());
		graph.put(course, prereqList);
	}
}