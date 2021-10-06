/*
	Insert a character
	Delete a character
	Replace a character
*/

/*
	T/S - O(3^N)/Size of recursion stack
*/
String word1, word2;
int[][] cache;
public int minDistanceRecursive(String word1, String word2) {
	this.word1 = word1;
	this.word2 = word2;
	this.memo = new int[word1.length()+1, word2.length()+1] 
	return minDistanceRecursive(0,0);
}

public int minDistanceRecursive(int i, int j) {
	int m = word1.length();
	int n = word2.length();

	// Base cases
	if(m == 0)
		cache[i][j] = n;

	if(n == 0)
		cache[i][j] = m;

	if(this.word1.charAt(i) == this.word2.charAt(j))
		cache[i][j] = minDistanceRecursive(i+1, j+1); // move both without adding any cost

	// Recurrence relation
	int insertionCost = 1 + minDistanceRecursive(i, j+1); // we insert a mismatched character at i, and then check for rest from s2 from j+1 onwards
	int deletionCost = 1 + minDistanceRecursive(i+1, j); // we delete a character from s1, that means we move 1 forward, so i+1
	int updationCost = 1 + minDistanceRecursive(i+1, j+1); // we updated a character in s1 to look like character in s2, so we move both

	cache[i][j] = Math.min(insertionCost, Math.min(deletionCost, updationCost));

	return cache[i][j]
}

/*
	Optimized apprach using Dynamic Programming
*/

public int minDistance(String word1, String word2) {
	int m = word1.length();
	int n = word2.length();

	int[][]dp = new int[m][n];


}

public int minDistance(int i, int j) {
	


	if(dp[i][j])
}