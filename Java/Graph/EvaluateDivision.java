class EvaluateDivision {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries){
        
        // First we create a Graph
        HashMap<String, HashMap<String, Double>> graph = new HashMap<>();

        // Build the graph
        for(int i=0; i<equations.size(); i++) {
            List<String> pair = equations.get(i);
            double value = values[i];

            String u = pair.get(0);
            String v = pair.get(1);
            
            if (!graph.containsKey(u))
                graph.put(u, new HashMap<String, Double>());
            if (!graph.containsKey(v))
                graph.put(v, new HashMap<String, Double>());

            graph.get(u).put(v, value);
            graph.get(v).put(u, 1 / value);
        }
            

        // Run each query via DFS to verify if there exists a path from dividend to divisor
        double[] results = new double[queries.size()];
        
        for(int i=0; i<queries.size(); i++) {
            List<String> query = queries.get(i);
            String dividend = query.get(0), divisor = query.get(1);
            
            if (!graph.containsKey(dividend) || !graph.containsKey(divisor))
                results[i] = -1.0;
            else if (dividend == divisor)
                results[i] = 1.0;
            else {
                HashSet<String> visited = new HashSet<>();
                results[i] = DFS(graph, dividend, divisor, 1, visited);
            }
        }
        return results;
    }
    
    private double DFS(HashMap<String, HashMap<String, Double>> graph, String src, String target, double product, Set<String> visited) {
        // Mark the node visited
        visited.add(src);
        double ans = -1.0;
        
        Map<String, Double> neighbors = graph.get(src);
        if(neighbors.containsKey(target)) {
            ans = product * neighbors.get(target);
        } else {
            for(Map.Entry<String, Double> pair : neighbors.entrySet()) {
                String nextNode = pair.getKey();
                if(visited.contains(nextNode)) 
                    continue;
                ans = DFS(graph, nextNode, target, product*pair.getValue(), visited);
                
                if(ans != -1.0) 
                    break;
            }
        }
        
        // Unmark the visited node for next set of backtracking
        visited.remove(src);
        return ans;  
    }
    
    
}
