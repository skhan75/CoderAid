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
	 	
	 	return canPartitionOptimizedUtil(num, dp, sum/2, 0);
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
	

	public static void main(String[] args) {
		EqualSubsetSumPartition sp = new EqualSubsetSumPartition();

		int[] input = {1, 1, 3, 4, 7};
		System.out.println(sp.canPartitionRecursive(input));
		System.out.println(sp.canPartitionOptimizedTopDown(input));

		input = new int[]{2, 3, 4, 6};
		System.out.println(sp.canPartitionRecursive(input));
		System.out.println(sp.canPartitionOptimizedTopDown(input));
	}



}