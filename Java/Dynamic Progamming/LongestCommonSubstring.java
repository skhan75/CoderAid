class LongestCommonSubstring {

	int longestCommonSubstring(String s1, String s2) {

		int[][] dp = new int[s1.length()+1][s2.length()+1];
		int count = 0;

		for(int i=1; i<=s1.length(); i++) {
			
			for(int j=1; j<=s2.length(); j++) {
				
				if(s1.charAt(i-1) == s2.charAt(j-1)) {
					dp[i%2][j] = 1 + dp[(i-1)%2][j-1];
					count = Math.max(count, dp[i%2][j]);
				}

			}
			
		}

		return count;
	}
 
	int longestCommonSubstringRecursive(String s1, String s2) {
		return lcs(s1,s2,s1.length(),s2.length(),0);
	}

	private int lcs(String s1, String s2, int i, int j, int count) {

		// base case
		if(i==0 || j==0) 
			return count;


		// descision
		if(s1.charAt(i-1) == s2.charAt(j-1)) 
			count = lcs(s1,s2, i-1, j-1, count+1);

		count = Math.max(count, 
			Math.max(
				lcs(s1, s2, i, j - 1, 0), 
				lcs(s1, s2, i - 1, j, 0)
		));
		

		// return
		return count;

	}


	public static void main(String[] args) {
		LongestCommonSubstring lcs = new LongestCommonSubstring();
		String s1 = "abcdaf";
		String s2 = "zbcdf";
		System.out.println("LCS " + lcs.longestCommonSubstring(s1, s2));
	}
}