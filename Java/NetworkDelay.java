
public int networkDelay(int[][] times, int n, int k) {

	Map<Integer, List<int[]> graph = new HashMap<>();

	for(int[] edge : times) {
		int u = edge[0]
		int v = edge[1];
		int wt = edge[2];

		if(!graph.contains(u))
			graph.put(u, new ArrayList<int[]>());

		graph.get(u).add(new int[]{v, wt});
	}

	PriorityQueue<int[]> minheap = new PriorityQueue<>();

	// Add the cost at source k to the min heap 
	minheap.add(new int[]{0, k})

	Map<Integer, Integer> dist = new HashMap<>();

	while(!minheap.isEmpty()) {

		int[] target = minheap.poll();
		int d = target[0];
		int node = target[1];

		if(dist.containsKey(node))
			continue;

		dist.put(node, d);

		if(graph.containsKey(node)) {
			// explore neighbors of this target
			for(int[] edge : graph.get(node)) {
				int nei = edge[0];
				int d2 = edge[1];

				if(!dist.containsKey(nei))
					minheap.offer(new int[]{d+d2, nei})
			}
		}
	}

	if(dist.size!=n)
		return -1

	int ans = 0;

	for(int d : dist.values()){
		ans = Math.max(ans, d);
	}

	return ans;

}