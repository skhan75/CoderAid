import java.util.*;

class LongestIncreasingSubsequence {

	class LIS {
		int count;
		ArrayList<Integer> subsequence;

		LIS (int count, ArrayList<Integer> subsequence) {
			this.count = count;
			this.subsequence = subsequence; 
		}
	}

	public LIS longestIncreasingSubsequence(int[] A) {
		int[] dp = new int[A.length];
		int[] solutionArray = new int[A.length];

		// Fill the dp array with 1s, as the LIS you can make with just one element is 1
		for(int i=0; i<A.length; i++) {
			dp[i] = 1;
			solutionArray[i] = i;
		}

		for(int i=1; i<A.length; i++) {
			for(int j=0; j<i; j++) {
				if(A[j] < A[i]) {
					// Add 1 to signify the longest found so far
					if(dp[j]+1 > dp[i]) {
						dp[i] = dp[j]+1;
						// Solution to i is coming from j
						solutionArray[i] = j;
					}
				}
			}
		}


		// Now we find the maximum item from dp, which will be the count of LIS
		int maxValue=0;
		int maxIndex=0;
		for(int i=0; i<dp.length; i++) {
			if(dp[i] >= dp[maxIndex]) {
				maxIndex = i; 
				maxValue = dp[i];
			} 
		}

		// Extract the solution array 
		int i = maxIndex;
        int next = maxIndex;
        ArrayList<Integer> lis = new ArrayList();

        do {
        	i = next;
        	lis.add(A[i]);
        	next = solutionArray[i];
        } while(i != next);

        // reverse to get in the increasing order
        Collections.reverse(lis);
      
		return new LIS(maxValue, lis);
	}

	
	public static void main(String[] args) {
		LongestIncreasingSubsequence lis = new LongestIncreasingSubsequence();

		int[] arr1 = {3, 10, 2, 11};

		LIS lisResult = lis.longestIncreasingSubsequence(arr1);
		System.out.println("Length of Longest Increasing Sub Sequence is " + lisResult.count);
		System.out.println("Longest Increasing Sub Sequence is " + lisResult.subsequence.toString());

		LIS lisResult1 = lis.longestIncreasingSubsequenceOptimal(arr1);
		System.out.println("Length of Longest Increasing Sub Sequence is " + lisResult1.count);
		System.out.println("Longest Increasing Sub Sequence is " + lisResult1.subsequence.toString());

	}
}