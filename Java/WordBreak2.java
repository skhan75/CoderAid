HashMap<String, List<String>> memo = new HashMap<>();

public List<String> wordBreak(String s, List<String> wordDict) {
	// Converting to Set to have a constant time lookup instead of linear
	return wordBreak(s, new HashSet<>(wordDict));
}

public List<String> wordBreak(String s, Set<String> wordDict) {

	List<String> result = new ArrayList<>();

	if(memo.contains(s))
		return memo.get(s);

	for(String word : wordDict) {
		String prefix = s.substring(0, word.length());

		if(prefix.equals(word)) {// That means we have found a starting word

			if(word.length() == s.length()) // That means we have exhausted all possibilities
				result.add(word);
			else {
				// Looking for other possible words
				List<String> temp = wordBreak(s.substring(word.length(), s.length()), wordDict);
				for(String t : temp)
					result.add(word + " " + t);
			}
		}
	}

	memo.put(s, result);

	return result;
}