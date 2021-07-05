class MaximumSubarraySum {

	/*
		Look at each index and calculate the maximum sum till that index.

		KADANE(A):
			maxCurrent = maxGlobal = A[0]
			for i from 1 to length(A) - 1:
				maxCurrent = max(A[i], maxCurrent + A[i])

				if maxCurrent > maxGlobal:
					maxGlobal = maxCurrent;

			return maxGloball

		Runtime --> O(N) where N is length of Arr
		Space --> O(1)
	*/

	public int kadane(int[] arr) {
		int maxCurrent = 0;
		int maxGlobal = Integer.MIN_VALUE;
		
		for(int i=1; i<arr.length; i++) {
			maxCurrent = Math.max(arr[i], maxCurrent + arr[i]);
			if(maxCurrent > maxGlobal)
				maxGlobal = maxCurrent;
		}

		return maxGlobal;
	}

	public static void main(String[] args) {
		MaximumSubarraySum mss = new MaximumSubarraySum();

		int[] arr = {-2, -3, 4, -1, -2, 1, 5, -3};
		System.out.println("Maximum Subarray Sum is " + mss.kadane(arr));

	}
	
}