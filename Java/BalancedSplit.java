import java.util.*;

class BalancedSplit {

	public int findSplitPoint(int[] arr) {
		int n = arr.length;

		Arrays.sort(arr);

		// traverse array element and compute sum
	    // of whole array
	    int leftSum = 0;
	     
	    for (int i = 0 ; i < n ; i++)
	        leftSum += arr[i];
	 
	    // again traverse array and compute right
	    // sum and also check left_sum equal to
	    // right sum or not
	    int rightSum = 0;
	     
	    for (int i = n-1; i >= 0; i--)
	    {
	        // add current element to right_sum
	        rightSum += arr[i];
	 
	        // exclude current element to the left_sum
	        leftSum -= arr[i] ;
	 
	        if (rightSum == leftSum)
	            return i ;
	    }
	 
	    // if it is not possible to split array
	    // into two parts.
	    return -1;
	}

	boolean isBalancedSplit(int[] arr) {
		return findSplitPoint(arr) != -1;
	}

	public static void main(String[] args) {
		BalancedSplit b = new BalancedSplit();
		int arr[] = {1,5,7,1};
    	
		System.out.println(b.isBalancedSplit(arr));
	}
}