/* 
	0/1 Knapsack
	Given the weights and profits of N items we are asked to put these items in a knapsack that has a capacity C. 
	The goal is to get the maximum profit from the items in the knapsack. 
	Each item can only be selected once as we dont have the multiple quantites of any item
*/

public class Knapsack {
	/*
		Complexity: O(2^n)
		Optimal Sub-structure: To consider all subsets of items, there can be two cases for every item. 

		Case 1: The item is included in the optimal subset.
		Case 2: The item is not included in the optimal set.

		A basic brute force solution could be try all combinations of the given items allowing to choose the 
		one with the maximum profit and a weight that doesnt exceed C. 

		https://www.youtube.com/watch?v=mGfK-j9gAQA
	*/
	int solveKnapsackRecursive(int[] profits, int[] weights, int capacity) {
		return knapsackRecursive(profits, weights, capacity, 0);
	}

	// Returns the maximum value that can be put in a knapsack of capacity W
	static int knapsackRecursive(int[] profits, int[] weights, int capacity, int currentIndex) {

		// base case
		if(capacity<=0 || currentIndex>=profits.length) {
			return 0;
		}

		// if the weight of the nth item is more than Knapsack capacity ,
		// then this item cannot be included in the optimal solution
		if(weights[currentIndex] > capacity) return knapsackRecursive(profits, weights, capacity, currentIndex+1);

		// Return the maximum of two cases
		// 1. nth item included
		// 2. not included
		else return Math.max(
			profits[currentIndex] + knapsackRecursive(profits, weights, capacity-weights[currentIndex], currentIndex+1),
			knapsackRecursive(profits, weights, capacity, currentIndex+1)
		);
	}

	// Runtime --> O(NW) Space --> O(NW)
	static int knapsackTimeOptimized(int[] profits, int[] weights, int capacity) {

		int n = profits.length;
		int[][] dp = new int[n+1][capacity+1];

		// Iterate for every picked element and build dp[][] in bottom up manner
		for(int i=1; i<=n; i++) {

			for(int w=1; w<=capacity; w++) {

				if(weights[i-1] <= w) {
					dp[i][w] = Math.max(
						// Including current weight and subtracting it from total weight 
						profits[i-1] + dp[i-1][w - weights[i-1]],
						// excluding current weight
						dp[i-1][w]
					);
				} else {
					// If there is no space/capacity left, return what you have already gotten with that i-1,w pair
					dp[i][w] = dp[i-1][w];
				}
			}
		}
		return dp[n][capacity];
	}

	/*
		Since we can see from the memoized dp array, that we are alternating between i-1 and ith values.
		Therefore it would be safe to consider that we just need 2 rows to keep track of the corresponding values
		
		Runtime --> O(NW) Space --> O(2n)~ O(n)

		We replace i-1 % 2 with i+1 % 2, as both return the same value. Its done to avoid when i = 0, 
		it will return wrong answer

		https://www.youtube.com/watch?v=7C_FIc7PytA
	*/
	static int knapsackTimeAndSpaceOptimized(int[] profits, int[] weights, int capacity) {

		int n = profits.length;
		int[][] dp = new int[2][capacity+1];

		for(int i=1; i<=n; i++) {
			for(int w=1; w<=capacity; w++) {
				if(weights[i-1] <= w) {
					dp[i%2][w] = Math.max(
						profits[i-1] + dp[(i+1)%2][w - weights[i-1]],
						dp[(i+1)%2][w]
					);
				} else {
					dp[i%2][w] = dp[(i+1)%2][w];
				}
			}
		}
		return dp[1][capacity];
	}
	
	public static void main(String[] args) {
		Knapsack ks = new Knapsack();
		
		int[] profits1 = {1, 6, 10, 16};
    	int[] weights1 = {1, 2, 3, 5};
    	int maxProfit1 = ks.solveKnapsackRecursive(profits1, weights1, 7);
    	System.out.println("Total knapsack profit ---> " + maxProfit1);

    	int[] profits2 = { 60, 100, 120 };
    	int[] weights2 = { 10, 20, 30 };
    	int maxProfit2 = ks.solveKnapsackRecursive(profits2, weights2, 50);
    	System.out.println("Total knapsack profit ---> " + maxProfit2);

    	int[] profits3 = { 60, 100, 120 };
    	int[] weights3 = { 10, 20, 30 };
    	int maxProfit3 = ks.knapsackTimeOptimized(profits3, weights3, 50);
    	System.out.println("Total knapsack profit ---> " + maxProfit3);

    	// Runtime --> O(NW) Space --> O(2n)~ O(n)
    	int maxProfit4 = ks.knapsackTimeAndSpaceOptimized(profits3, weights3, 50);
    	System.out.println("Total knapsack profit ---> " + maxProfit4);
	}

}


