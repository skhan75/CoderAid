
/*
	MIN (
		- Add a character ( Adding a character in the first string is similar to deleting a character in the second string)
			-  Since we want to stay within the bounds of the given lengths without adding additional character to first string,
			   we intuitively delete a character from the second string.
			   f(i, j-1) + Cost_Addition
		- Delete a character from first string
			   f(i-1, j) + Cost_Deletion
		- Change/Transition a character 
			   f(i-1, j-1) + Cost_Transition
	)

	https://www.youtube.com/watch?v=XJ6e4BQYJ24
 */

public class EditDistance {

	// Uses bottom up DP to find the edit distance
	int minimumEditDistance(char[] s1, char[] s2) {
		int dp[][] = new int[s1.length+1][s2.length+1];
		int row = dp[0].length, col = dp.length;

		// Fill 0th rows with ith values
		for(int i=0; i<row; i++){ 	
			dp[0][i] = i; 
		}

		for(int i=0; i<col; i++) {
			dp[i][0] = i;
		}

		for(int i=1; i<=s1.length; i++) {
			for(int j=1; j<=s2.length; j++) {
				if(s1[i-1] == s2[j-1]) {
					dp[i][j] = dp[i-1][j-1];
				} else {
					dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]);
				}
			}
		}

		return dp[s1.length][s2.length];

	}

	private int min(int a, int b, int c) {
		int t = Math.min(a,b);
		return Math.min(c,t);
	}

	public static void main(String[] args) {
		EditDistance editDistance = new EditDistance();

		String s1 = "azced";
		String s2 = "abcdef";
		System.out.println("Minimum number of edits to convert " + s1 + " to " + s2 + " is " + 
			editDistance.minimumEditDistance(s1.toCharArray(), s2.toCharArray()));

		String s3 = "helpo";
		String s4 = "hello";
		System.out.println("Minimum number of edits to convert " + s3 + " to " + s4 + " is " + 
			editDistance.minimumEditDistance(s3.toCharArray(), s4.toCharArray()));
	}
}