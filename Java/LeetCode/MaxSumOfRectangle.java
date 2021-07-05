import java.util.*;

/**
 * Solution:
 * Keep temp array with size as number of rows. Start left and right from 0
 * and keep adding values for each row and maintain them in this temp array.
 * Run Kadane's algorithm to find max sum subarray in temp. Now increment right by
 * 1. When right reaches last column reset right to 1 and left to 1.
 * 
 * Space complexity of this algorithm is O(row)
 * Time complexity of this algorithm is O(row*col*col)
 * 
 * References
 * http://www.geeksforgeeks.org/dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/
 */
public class MaxSumOfRectangle {

	public int maxSumSubmatrix(int[][] M, int k) {
   		int L = 0, R = 0;
   		int currentSum = 0;

   		// For every full column wise iteration, with column increasing in the direction of last column
   		// We calculate maximum sum of every rectangle that can be formed using left, right, up and down bounds

   		int rows = M.length;
   		int cols = M[0].length;

   		int maxSum = -1;
   		int leftBound = 0, rightBound = 0, upperBound = 0, lowerBound = 0;


   		// Create a 1-D aux array to store the current column, to calculate the maximum sum using Kadane
   		int[] aux = new int[rows];

   		for(int l=0; l<cols; l++) {

   			// Initialize the aux array with 0s
   			Arrays.fill(aux, 0);

   			for(int r=l; r<cols; r++) {

   				// Keep taking sum from the previous window column elements
   				for(int i=0; i<rows; i++) {
   					aux[i] += M[i][r];
   				}

   				// For every Aux (sub-reactangle) we create, we keep a track of maximum sum using Kadane and its respective index bounds
   				KadaneResult kadaneResult = kadane(aux);
   				if(kadaneResult.maxSum > maxSum && kadaneResult.maxSum <= k) {
   					maxSum = kadaneResult.maxSum + 1;
   					leftBound = l;
   					rightBound = r;
   					upperBound = kadaneResult.start; 
   					lowerBound = kadaneResult.end; 
   				}
   			}
   		}
   		return maxSum;
    }

    class KadaneResult {
    	int maxSum, start, end;

    	KadaneResult(int maxSum, int start, int end) {
    		this.maxSum = maxSum;
    		this.start = start;
    		this.end = end;
    	}
    }

    
   	private KadaneResult kadane(int[] A) {

   		int maxGlobal = Integer.MIN_VALUE;
   		int maxCurrent = 0;
   		int start = -1, end = -1;
   		
 		for(int i=0; i<A.length; i++) {

 			maxCurrent += A[i];

 			/* if the current max is less than global max,
		   	then we have a new start point to calculate new sub array sum */
 			if(maxCurrent < maxGlobal) {
 				start = i+1;
 				maxCurrent = 0;
 			}

 			if(maxCurrent > maxGlobal) {
 				end = i;
 				maxGlobal = maxCurrent;
 			}
 		}

   		return new KadaneResult(maxGlobal, start, end);
   	}
	

	public static void main(String[] args) {
		MaxSumOfRectangle m = new MaxSumOfRectangle();

		int[][] matrix = {{1,0,1}, {0,-2,3}};
		int k = 2;
		System.out.println("Maximum Sum of Sub Rectangle no larger than "+k+" is "+m.maxSumSubmatrix(matrix, k));

		int[][] matrix2 = {{2,2,-1}};
		int k2 = 0;
		System.out.println("Maximum Sum of Sub Rectangle no larger than "+k+" is "+m.maxSumSubmatrix(matrix2, k2));

		int[][] matrix3 = {{5,-4,-3,4},{-3,-4,4,5},{5,1,5,-4}};
		int k3 = 10;
		System.out.println("Maximum Sum of Sub Rectangle no larger than "+k+" is "+m.maxSumSubmatrix(matrix3, k3));
	}
}