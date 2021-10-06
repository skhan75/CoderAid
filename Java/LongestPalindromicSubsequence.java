public int longestPalindromeSubsequence(String s) {
	return lps(s.toCharArray(), 0, s.length() - 1);
}

private int lps(char[] s, int i, int j) {

	if(i > j)
		return 0; // not possible

	if(i == j)
		return 1; // when there is only one character

	if(s[i] == s[j])
		return 2 + lps(s, i+1, j-1);


	int max = Math.max(lps(s, i+1, j), Math.max(lps(s, i+1, j-1), lps(s, i, j-1)));
}