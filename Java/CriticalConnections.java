
List<Integer>[] graph;
List<List<Integer>> criticalConnections;
int[] visitedTimes;
int[] lowTimes;
int time;


public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {

    graph = new ArrayList[n];
    criticalConnections = new ArrayList<>();
    visitedTimes = new int[n];
    lowTimes = new int[n];

    // build adjacency list graph
    buildGraph(connections);

    boolean[] visited = new boolean[n];

    dfs(visited, 0, -1); // starting node, parent

    return criticalConnections;     
}

// Post order dfs (Tarjan's Algorithm)
private void dfs(boolean[] visited, int currNode, int parent) {

    visited[currNode] = true;

    // Mark the visited/discovery time and low times
    visitedTimes[currNode] = lowTimes[currNode] = time++;

    // Explore the neighbors
    for(int neighbor : graph[currNode]) {

        if(neighbor == parent) // dont want to explore back to parent because we came from there
            continue;

        if(!visited[neighbor]){
            dfs(visited, neighbor, neighbor, currNode);

            lowTimes[currNode] = Math.min(lowTimes[currNode], lowTimes[neighbor]);

            if(visitedTimes[currNode] < lowTimes[neighbor])
                criticalConnections.add(Arrays.asList(currNode, neighbor));

        } else { // This means that we have a neighbor that has already been visited, and this is the back edge
            lowTimes[currNode] = Math.min(lowTimes[currNode], visitedTimes[neighbor]);
        }
    }
}

private void buildGraph(List<List<Integer>> connections) {
    // Initialize graph nodes
    for(int i=0; i<graph.length; i++)
        graph[i] = new ArrayList<>();

    // Build graph
    for(List<Integer> connection : connections) {
        int u = connection.get(0);
        int v = connection.get(1);

        graph[u].add(v);
        graph[v].add(u);
    }
}