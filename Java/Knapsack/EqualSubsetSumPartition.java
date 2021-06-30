public class EqualSubsetSumPartition {

	 public boolean canPartitionRecursive(int[] num) {
	 	int sum=0;
	 	for(int i=0; i<num.length; i++) sum += num[i];

	 	// If sum is an odd numbe, we can't have two subsets with equal sum
	 	if(sum%2!=0) return false;

	 	return canPartitionUtil(num, sum/2, 0);
	 }

	 /* Brute Force:
	 	Try all the combinations of partitioning of the given numbers into two sets to see 
	 	if any of the two sets have an equal sum
	 	
	 	Runtime --> O(2^n) Space --> O(n) 
	 */
	 private boolean canPartitionUtil(int[] num, int sum, int currentIndex) {
	 	// base check
	 	if(sum==0) return true;
	 	// out of bounds
	 	if(num.length==0 || currentIndex>=num.length) return false;
	 	
	 	// if currentIndex is greater than sum, then this index cannot be included in set
	 	if(num[currentIndex]>sum) return canPartitionUtil(num, sum, currentIndex+1);

	 	/* 
	 	Recursively check if there is any pair of subset available with equal sums
	 	 	1. Check by including the current number
	 	 	2. Check by excluding the number
	 	*/
	 	return canPartitionUtil(num, sum - num[currentIndex+1], currentIndex+1) 
	 		|| canPartitionUtil(num, sum, currentIndex+1);
	 }


	 /*
	 	Dynamic Programming - Top Down
	 	Runtime --> O(NS) Space --> O(NS)
	 */
	 public boolean canPartitionOptimizedTopDown(int[] num) {
	 	int sum=0;
	 	for(int i=0; i<num.length; i++) sum += num[i];

	 	// If sum is an odd numbe, we can't have two subsets with equal sum
	 	if(sum%2!=0) return false;

	 	Boolean[][] dp = new Boolean[num.length][sum/2 + 1];
	 	
	 	return canPartitionOptimizedTopDownUtil(num, dp, sum/2, 0);
	 }

	 private boolean canPartitionOptimizedTopDownUtil(int[] num, Boolean[][] dp, int sum, int currentIndex) {

	 	// base condition
	 	if(sum == 0) return true;
	 	// out of bounds
	 	if(num.length==0 || currentIndex>=num.length) return false;

	 	// If we have not processed a similar problem
	 	if(dp[currentIndex][sum] == null) {
			// if currentIndex is greater than sum, then this index cannot be included in set
	 		if(num[currentIndex]>sum) return canPartitionOptimizedTopDownUtil(num, dp, sum, currentIndex+1);
	 		
	 		dp[currentIndex][sum] = canPartitionOptimizedTopDownUtil(num, dp, sum - num[currentIndex], currentIndex+1)	 
	 			|| canPartitionOptimizedTopDownUtil(num, dp, sum, currentIndex+1);																			
	 	}

	 	return dp[currentIndex][sum];
	 }

	  /*
	 	Dynamic Programming - Bottom Up
	 	Runtime --> O(NS) Space --> O(2N) ~ O(N)
	 */
	 public boolean canPartitionOptimizedBottomUp(int[] num) {
	 	int n = num.length;

	 	int sum=0;
	 	for(int i=0; i<num.length; i++) {
	 		sum += num[i];
	 	}

	 	if(sum%2!=0) return false; 

	 	// We need to find subsets with equal halved sum
	 	sum /= 2;
    	boolean[][] dp = new boolean[2][sum + 1];
	 
	 	// Fill n Rows --> Populate the sum=0 column as true, as we can have 0 sum without including any element 
	  	for(int i=0; i < 2; i++)
      		dp[i][0] = true;

	 	// Fill 0th Row --> Populate all sum columns as false, when there is one element 
	 	// Only if that one element is equal to the required sum, then mark it as true 
	 	for(int s=1; s <= sum ; s++) {
	    	dp[0][s] = (num[0] == s ? true : false);
	    }

	 	// Process all subsets for all sums 
	 	for(int i=1; i<n; i++) {
	 		for(int s=1; s<=sum; s++) {
	 			// If we can get the sum already without current ith number, we take it from the dp 
	 			if(dp[(i-1)%2][s]) 
	 				dp[i%2][s] = dp[(i-1)%2][s];
	 			else if(s >= num[i])
	 				dp[i%2][s] = dp[(i-1)%2][s - num[i]];
	 		}
	 	}

	 	return dp[(n-1)%2][sum];
	 }
	

	public static void main(String[] args) {
		EqualSubsetSumPartition sp = new EqualSubsetSumPartition();

		int[] input = {1, 1, 3, 4, 7};
		System.out.println(sp.canPartitionRecursive(input));
		System.out.println(sp.canPartitionOptimizedTopDown(input));
		System.out.println(sp.canPartitionOptimizedBottomUp(input));

		input = new int[]{2, 3, 4, 6};
		System.out.println(sp.canPartitionRecursive(input));
		System.out.println(sp.canPartitionOptimizedTopDown(input));
	}

}