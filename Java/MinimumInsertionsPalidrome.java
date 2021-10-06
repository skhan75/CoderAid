import java.util.*;

class MinimumInsertionPalindrome {

	public int minInsertions(String s) {
       char[] sc = s.toCharArray();
       int n = sc.length;

       return n - lcs(sc);
       // Answer --> Length of the string - Lcngest common subsequence 
    }

    private int lcs(char[] s) {
    	int[][] dp = new int[s.length][s.length];
    	int n = s.length;

    	for(int i=0; i<s.length; i++)
    		dp[i][i] = 1;

    	for(int l=2; l<=n; l++) {
    		for(int i=0; i<n-l+1; i++) {
    			int j = i+l-1;

    			if(l==2 && s[i] == s[j])
    				dp[i][j] = 2;
    			else if(s[i] == s[j]) 
    				dp[i][j] = 2 + dp[i+1][j-1];
    			else
    				dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]);
    		}
    	}

    	return dp[0][n-1];
    	
    }



	public static void main(String[] args) {
		MinimumInsertionPalindrome m = new MinimumInsertionPalindrome();
		String s = "zjveiiwvc";
		System.out.println(m.minInsertions(s));
	}
}