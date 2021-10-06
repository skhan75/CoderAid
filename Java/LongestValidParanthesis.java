public int longestValidParanthesis(String s) {


	// iterate from left to right and check what's the maximum you can make

	int left=0, right=0, maxans=0;

	for(int i=0; i<s.length(); i++) {
		if(s.charAt(i) == '(')
			left++;
		else
			right++;

		if(right == left)
			maxans = Math.max(maxans, 2*right);
		else if(right > left) // reset
			left = right = 0;
	}

	for(int i=s.length()-1; i>=0; i--) {
		if(s.charAt(i) == '(')
			left++;
		else
			right++;

		if(left==right)
			maxans = Math.max(maxans, 2*right);
		else if(left >= right)
			left = right = 0;
	}

	return maxans;
}