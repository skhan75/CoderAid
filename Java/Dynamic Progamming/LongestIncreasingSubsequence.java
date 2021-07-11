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

	

	/* 	Uses Patience Sort along with Binary Search
		Runtime Complexity --> O(NlogN)
		Space Complexity --> O(N) 	*/
	public LIS longestIncreasingSubsequenceOptimal(int[] A) {

		// holder will store the temporary intermediate result
		// Stores minimum of the last value of increasing subsdequence of particular length
		int[] holder = new int[A.length];
		// store the final result
		int[] result = new int[A.length];

		// Initialize the result with all -1s
		for (int i=0; i<result.length;i++ ) {
			result[i] = -1;
		}

		// Put the first index in the left most holder
		holder[0] = 0;

		int len = 0;

		for(int i=1; i<A.length; i++) {
			if(A[holder[0]] > A[i]) {
				holder[0] = i;
			} else if(A[holder[len]] < A[i]) { // If A[i] is greater than the last value in the holder, then put/append it in holder at that len
				len++;
				holder[len] = i; 
				result[holder[len]] = holder[len-1]; // Result will store where last value at particular holder is coming from
			} else { // Else we do a Binary Search to fdind the ceiling of A[i] and place it at that holder location
				int ceilIndex = getCeilIndex(A, holder, len, A[i]);
				holder[ceilIndex] = i;
				result[holder[ceilIndex]] = holder[ceilIndex-1];
			}
		}

		ArrayList<Integer> subsequence = new ArrayList();
		int current = holder[len];
		while(current!=-1) {
			subsequence.add(A[current]);
			current = result[current];
		}

		// reverse to get in the increasing order
        Collections.reverse(subsequence);

		return new LIS(len+1, subsequence);

	}

	private int getCeilIndex(int[] A, int[] holder, int end, int s) {
		int start = 0;
		int mid;
		int len=end; 

		while(start <= end) {
			mid = (start + end) / 2;
			if(mid < len && A[holder[mid]] < s && s<=A[holder[mid+1]]) { // Answer
				return mid+1;
			} else if(A[holder[mid]] < s) {
				start = mid + 1;
			} else {
				end = mid - 1;
			}
		}

		return -1;
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