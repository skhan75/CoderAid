Map<Character, List<Character>> graph = new HashMap<>();
LinkedList<Character> ordering = new LinkedList<>();

public String alienOrder(String[] words) {
	

	// create a graph with all the characters
	for(String word : words) 
		for(char c : word.toCharArray())
			graph.put(c, new ArrayList<>());
	

	// Build edges
	for(int i=0; i<words.length; i++) {

		String word1 = words[i];
		String word2 = words[i+1];

		// check if word2 is not a prefix of word1
		if(word2.length() < word1.length() && word1.startsWith(word2))
			return "";

		// Find the first non match and insert the relation into the graph
		for(int j=0=; j<Math.min(word1.length(), word2.length()), j++) {
			if(word1.charAt(j)!=word2.charAt(j)) {
				graph.get(word1.charAt(j)).add(word2.charAt(j));
				break;
			}
		}
	}


	// Post order DFS to build topological ordering
	for(Character c : graph.keySet()) {
		boolean result = dfs(c);
		if(!result) return "";
	}

	if(ordering.size() < graph.size())
		return "";

	return ordering.stream().map(String::valueOf).collect(Collectors.joining());
}


boolean dfs(Character c) {

	if(seen.containsKey(c))
		return seen.get(c); // cycle was detected

	seen.put(c, false);

	for(Character nei : graph.get(c)){
		boolean result = dfs(nei);
		if(!result) return false;
	}

	seen.put(c, true);
	ordering.addFirst(c);

	return true;
}





