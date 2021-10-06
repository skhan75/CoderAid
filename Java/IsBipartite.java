public boolean isBipartite(int[][] graph) {

	int[] color = new int[graph.length];

	// Color with DFS
	for(int i=0; i<graph.length; i++) {
		if(color[i] == 0 && !isValidColor(grpah, color, 1, i))
			return false
	}

	return true;
}

private boolean isValidColor(int[][] graph, int[] color, int currentColor, int node) {

	if(color[node] != 0)
		return color[node] == currentColor;

	color[node] = currentColor;

	for(int nei : graph[node]) {
		if(!isValidColor(graph, color, -currentColor, nei))
			return false;
	}


	return true;


}