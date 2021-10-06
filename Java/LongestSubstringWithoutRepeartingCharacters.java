/*
	Time --> O(2N)
	Space --> O(min(m,n))
*/
public int lengthOfLongestSubstring(String s) {

	int[] lastIndex = new int[128];

	int left = 0, right = 0;
	int res = 0;

	while(right < s.length()) {
		char rightChar = s.charAt(right);
		Integer index = lastIndex[rightChar];

		// If there is already an index value for the same character
		// We move our left point by 1, so as to remove that duplicate 
		if(index!=null && index>=left && index<right) 
			left = index+1;

		res = Math.max(res, right - left + 1);
		
		lastIndex[rightChar] = right;
		right++;
	}
	return res;
}

/*
	Time --> O(2N)
	Space --> O(min(m,n))
*/
public int lengthOfLongestSubstring(String s) {
	int n = s.length();
	int ans = 0;

	Map<Character, Integer> map = new HashMap<>();

	for(int j=0, i=0; j<n; j++) {
		if(map.containsKey(s.charAt(j))) 
			i = Math.max(map.get(s.charAt(j), i));
		
		ans = Math.max(ans, j - i + 1);
		map.put(s.charAt(j), j+1);
	}
	return ans;
}