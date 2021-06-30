// Find a subset whose sum is equal to the given sum

class SubsetSum {

	// Runtime O(N) Optimized Space --> O(2N)_
	public boolean canPartition(int[] nums, int sum) {
		int n = nums.length;

		boolean[][] dp = new boolean[2][sum+1];

		// populate the sum=0 column with true, as we can always form 0 sum with an empty set
		for(int i=0; i<2; i++) {
			dp[i][0] = true;
		}

		// with only one number, we can only for a subset when the number itself is equal to required sum
		for(int s=1; s<=sum; s++) {
			dp[0][s] = (nums[0] == s ? true : false);
		}

		// Process all remaining subsets
		for(int i=1; i<n; i++) {
			for(int s=1; s<=sum; s++) {
				// If the sum has already been reached without the current index i, then we return from previous
				if(dp[(i-1)%2][s]) {
					dp[i%2][s] = dp[(i-1)%2][s];
				} else if(nums[i] <= s) {
					// else include the number 
					dp[i%2][s] = dp[(i-1)%2][s - nums[i]];
				}
			}
		}

		return dp[n%2][sum];
	}

	public static void main(String[] args) {
		SubsetSum ss = new SubsetSum();
	    int[] num = { 1, 2, 3, 7 };
	    System.out.println(ss.canPartition(num, 6));
	    num = new int[] { 1, 2, 7, 1, 5 };
	    System.out.println(ss.canPartition(num, 10));
	    num = new int[] { 1, 3, 4, 8 };
	    System.out.println(ss.canPartition(num, 6));
	}
}