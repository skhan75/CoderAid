// Given a rod of length L, what is the maximum profit by selling different cuts of the lengths of rod
public class RodCutting {

	private int getMaximumProfit(int[] prices, int rodLength) {

		/*
			Here dp[i] indicates the maximum profit we can achieve with a knapsack capacity of i.

			Note that we use 1D array here which is different from classical knapsack 
			where we used 2D array. Here number of items never changes. 
			We always have all items available.
		*/
		int[] dp = new int[rodLength + 1];

		// Process for every legth of rod, what's the maximum profitable cuts that can be formed
		for(int l=1; l<=rodLength; l++) { // Here l --> current rod length
			for(int c=1; c<=l; c++) { // c --> current cut
				dp[l] = Math.max(dp[l], prices[c-1] + dp[l-c]); 
			}
		}

		return dp[rodLength];
	}

	public static void main(String[] args) {

		RodCutting rodCutting = new RodCutting();

		int rodLength = 4;
        int prices[] = {1, 5, 8, 9, 10, 17, 17, 20};
    	int maxProfit = rodCutting.getMaximumProfit(prices, rodLength);
    	System.out.println("Total Rod Cutting Profit ---> " + maxProfit);

	}
}