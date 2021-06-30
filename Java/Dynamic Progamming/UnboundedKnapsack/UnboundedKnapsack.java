import java.util.*;

// We can use same weight multiple times, provided we get the maximum profit.
public class UnboundedKnapsack {

	private int unboundedKnapsack(int[] profits, int[] weights, int capacity) {

		int n = profits.length;

		//Note that we use 1D array here which is different from classical knapsack 
		// where we used 2D array. Here number of items never changes. 
		// We always have all items available.
		int[] dp = new int[capacity + 1];

		for(int w=1; w<=capacity; w++) {
			for(int i=1; i<=n; i++) {
				if(profits[i-1] <= w) {
					dp[i] = Math.max(
						profits[i-1] + dp[i-weights[i-1]],
						dp[i-1]
					);
				}
			}
		}

		System.out.println("DP "+Arrays.toString(dp));
		return dp[capacity];
	}

	public static void main(String[] args) {

		UnboundedKnapsack uk = new UnboundedKnapsack();

		int C = 100;
        int profits[] = {10, 30, 20};
        int weights[] = {5, 10, 15};
    	int maxProfit = uk.unboundedKnapsack(profits, weights, C);
    	System.out.println("Total knapsack profit ---> " + maxProfit);

	}
}