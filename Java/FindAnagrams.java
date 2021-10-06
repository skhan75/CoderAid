public List<Integer> findAnagrams(String s, String p) {

	int[] phash = new int[26];
	int[] shash = new int[26];

	for(char c : p.toCharArray())
		phash[(int)(c - 'a')]++;


	List<Integer> output = new ArrayList<>();
	for(int i=0; i<s.length(); i++) {

		// Add count to shash
		shash[(int)(s.charAt(i) - 'a')]++;

		// we have to remove first character of the first batch of s
		if(i >= p.length())
			shash[(int)(s.charAt(i - p.length()) - 'a')]--;

		// Then we compare both arrays
		if(Arrays.equal(s, p))
			output.add(i - p.length() + 1);
	}

	return output;
}