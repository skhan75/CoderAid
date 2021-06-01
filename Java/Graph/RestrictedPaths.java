import java.util.*;

class RestrictedPaths {
    static final int MODULO = 1000000007;
    int[] dp;
    int n = 0;
    Boolean[] visited;
    Map<Integer, Integer> memo = new HashMap<>();

    public int countRestrictedPaths(int n, int[][] edges) {
        this.n = n;
        visited = new Boolean[n+1];
        Arrays.fill(visited, Boolean.FALSE);
        
        /** 1. First use Djikstra to find the shortest path from node 'n' to other nodes and store this
               information in a distance/weight map
        
            2. Then use DFS/Backtracking to calculate the no of restricted paths that satisfies the given relation using                the distance map we generated 
        **/
        
        // First we create a graph map containing nodes and their neighbors
        Map<Integer, List<int[]>> graphMap = new HashMap<Integer, List<int[]>>();
        
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int weight = edge[2];
            // Neighbors of u
            List<int[]> ul = graphMap.getOrDefault(u, new ArrayList<int[]>());
            // Neighbors of v
            List<int[]> vl = graphMap.getOrDefault(v, new ArrayList<int[]>());
            
            // Add v to the neighbors of u and vice versa
            ul.add(new int[]{v, weight});
            vl.add(new int[]{u, weight});
            
            graphMap.put(u, ul);
            graphMap.put(v, vl);
        }
        
        // Get the shortest paths map using Djikstra
        int[] distancesMap = getShortestDistances(n, graphMap);
        
        // DFS to calculate the no of restricted paths, starting from node 1
        int ans = DFS(distancesMap, graphMap, 1);

        return ans;
    }
    
    // O(ElogV)
    public int[] getShortestDistances(int n, Map<Integer, List<int[]>> map) {
        int[] distances = new int[n + 1];
        Arrays.fill(distances, Integer.MAX_VALUE);
        
        // Weight to last node is 0
        distances[n] = 0;

        PriorityQueue<Integer> priorityQueue = new PriorityQueue<Integer>(new Comparator<Integer>() {
            public int compare(Integer node1, Integer node2) {
                return distances[node1] - distances[node2];
            }
        });

        // Add the last node to PQ
        priorityQueue.offer(n);

        while (!priorityQueue.isEmpty()) {
            // Get the current node
            int node = priorityQueue.poll();
            
            // Add this node to visited list
            visited[node] = true;

            int distance = distances[node];

            // Get the neighbors of the current node
            List<int[]> neighbors = map.get(node);
            
            for (int[] neighbor : neighbors) {
                int nextNode = neighbor[0];
                int weight = neighbor[1];

                // If neighbor is not visited yet
                if(!visited[nextNode]) {
                    int newWeight = distance + weight;

                    // If the new weight is less than the existing weight on the neighbor node, that means we found a cheaper path
                    // So update the distances map with the new cheaper weight
                    if (newWeight < distances[nextNode]) {
                        distances[nextNode] = newWeight;
                        priorityQueue.offer(nextNode);
                    }
                }
            }
        }
        return distances;
    }
    
    // O(V)
    public int DFS(int[] distances, Map<Integer, List<int[]>> graph, int currentNode) {
        
        // Base case - When we have reached the last node, we return 1, as distance to itself is 1 unit
        if (currentNode == n) return 1;
        
        if (memo.get(currentNode) != null) return memo.get(currentNode);

        int ans = 0;

        // Get the neighbors of the current node
        List<int[]> neighbors = graph.get(currentNode);
        int currentDistance = distances[currentNode];

        for(int[] neighbor : neighbors) {
            int nextNode = neighbor[0];
            // If distance of the current node is greater than distance of the corresponding next node, then its a valid restricted path
            // P.S. Also we have ignored checking the duplication of the neighbors already seen because if a --> b satisfies the restricted path clause,
            // then by definition of restricted path b -X-> a will not be satisfied and will be ignored by the condition below
            if(distances[currentNode] > distances[nextNode]) {
                ans = (ans + DFS(distances, graph, nextNode)) % MODULO;
            }
        }

        memo.put(currentNode, ans);

        return ans;
    }   


    public static void main(String[] args) {
        int[][] edges = { {1,2,3}, {1,3,3}, {2,3,1}, {1,4,2}, {5,2,2}, {3,5,1}, {5,4,10} };
        RestrictedPaths rp = new RestrictedPaths();
        System.out.println("Number of restricted paths are: "+ rp.countRestrictedPaths(5, edges));
    }
    
}