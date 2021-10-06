public List<Integer> partitionLabels(String s) {

	List<Integer> output = new ArrayList<>();

	// Create a last occurence array, marking the last occurence of all the characters
	int[] last = new int[26];
	for(int i=0; i<s.length(); i++)
		last[s.charAt(i) - 'a'] = i;

	// itarate over s, and find the partition start and end indices and add it to the output
    // We add the start and end to the output, when i = end value
    // where end is the max last occurence of a character in a partition
    
    int start = 0, end = 0;
    for(int i=0; i<s.length(); i++) {
    	// we do a max to extend the partition if we encounter a character whose last occurence is greater than current character
    	end = Math.max(end, last[s.charAt(i) - 'a']);
    	if(i == end) {
    		output.add(i - start+1);
    		start = i+1;
    	}
    }

    return ans;

}