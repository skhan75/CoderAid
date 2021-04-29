import java.util.Arrays;

public class MaximumSlidingWindow {

	public int[] getMaxSlidingWindowBruteForce(int[] nums, int k) {
		int n = nums.length;

		// If either empty nums or k is 0, then return 0
		if(n*k == 0) return new int[0];

		int[] output = new int[n-k+1];

		// Iterate over blocks
		for(int i=0; i<n-k+1; i++){
			int max = Integer.MIN_VALUE;

			// Sliding over from i --> j, where j < i+k
			for(int j=i; j<i+k; j++){
				max = Math.max(max, nums[j]);
			}

			output[i] = max;
		}

		return output;
	}

	public int[] getMaxSlidingWindowDynamicProgramming(int[] nums, int k) {
		int n = nums.length;

		// If either empty nums or k is 0, then return 0
		if(n*k == 0) return new int[0];

		if(k==1) return nums;

		/* 
			Idea is to split the array into k blocks.
			The last block could contain less elements, if n%k != 0

			Lets use an array left, where left[j] will be the maximum element from left --> right direction
		 	Similalry we can use another auxillary array right, where right[j] is the maximum element, in the
		 	direction right --> left.

		 	left[j] = MAX(block_start --> j) left --> right
		 	right[j] = MAX(block_end --> j)	reverse order or right --> left

		 	max_window = MAX(left[j], right[j])
		*/

		int[] left = new int[n];
		int[] right = new int[n];
		int[] output = new int[n-k+1];

		left[0] = nums[0];
		right[n-1] = nums[n-1];

		for(int i=1; i<n; i++){
			// from left --> right
			if(i%k==0) left[i] = nums[i]; // start of another block 
			else left[i] = Math.max(left[i-1], nums[i]);

			// from right --> left (from reverse)
			int j = n-i-1;
			if(j%k==0) right[j] = nums[j];
			else right[j] = Math.max(right[j+1], nums[j]); // end of current block
		}

		
		//Now we are successfully able to create left and right arrays, which denote the window elements
		for(int j=0; j<n-k+1; j++) {
			output[j] = Math.max(left[j+k-1], right[j]);
		}

		return output;

	}

	public static void main(String[] args) {
		MaximumSlidingWindow maxSlidingWindow = new MaximumSlidingWindow();
		int[] input = {1,3,-1,-3,5,3,6,7};
		int k = 3;

		long startBf = System.nanoTime();
		int[] outputBruteForce = maxSlidingWindow.getMaxSlidingWindowBruteForce(input, k);
		long endBd = System.nanoTime();
		long elapsedTimeBf = (endBd - startBf);
		
		System.out.println("Maximum Sliding Window by Brute Force is " 
			+ Arrays.toString(outputBruteForce));
		System.out.println("Time taken "+elapsedTimeBf+" nano seconds");

		long startDp = System.nanoTime();
		int[] outputDynamic = maxSlidingWindow.getMaxSlidingWindowDynamicProgramming(input, k);
		long endDp = System.nanoTime();
		long elapsedTimeDp = (endDp - startDp);

		System.out.println("Maximum Sliding Window by DP is " 
			+ Arrays.toString(outputDynamic));
		System.out.println("Time taken "+elapsedTimeDp+" nano seconds");
	}
}