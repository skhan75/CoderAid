public boolean wordBreak(String s, List<String> wordDict) {
	Set<String> wordSet = new HashSet<>(wordDict);
	return backtrack(s, wordSet, 0, new Boolean[s.length()]);
}

// Space Complexity --> O(n) because depth of recursion tree can go up to n
// Time --> O(n3)
private backtrack(String s, Set<String> wordDict, int start, Boolean[] memo) {

	// base case
	if(start == s.length())
		return true;

	if(memo[start]!=null)
		return memo[start];

	// choice
	for(int end=start+1; end<s.length(); end++) {
		if(wordDict.contains(s.substring(start, end)) && backtrack(s, wordDict, end))
			memo[start] = true;
	}


	return memo[start];
}