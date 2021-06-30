
/*
	The change making problem addresses the question of finding number of coins (of certain denomination) 
	that add up to ad given amount of money M. It is a special case of Knapsack problem. 

	Given a list of denominations, and a target amount. What are the total number of combinations of the coins
	you can arrange to obtain the given amount. 
*/

public class CoinChange {

	private int getWays(int[] coins, int M) {

		int[] ways = new int[M+1];

		// There is only 1 ways to make 0 amount, so we set ways[0] = 1
		ways[0] = 1;

		// Go through all the coins 
		for(int c=0; c<coins.length; c++) {
			for(int m=0; m<=M; m++) {
				// The amount m has to be greater than current coin denomination for the coin to be added to ways
				if(coins[c] <= m) {
					ways[m] += ways[m - coins[c]];
				}
			}
		}

		return ways[M];
	}


	public static void main(String[] args) {
		CoinChange coinChange = new CoinChange();

		int[] coins = { 1, 5, 10 };
		int M = 12;
		System.out.println("Number of ways are --> " + coinChange.getWays(coins, M));

	}
}