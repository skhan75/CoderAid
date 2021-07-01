import java.util.*;

class MinimumCoinChange {

	/*
	 * FOR every coin c from 0 --> coins: dp[m] = min(dp[m], dp(m - coins[c]))
	 * min(without picking c'th coin, picking c'th coin)
	 */
	static int minCoins(int[] denominations, int M) {
		int[] dp = new int[M + 1];
		int n = denominations.length;
		Arrays.fill(dp, Integer.MAX_VALUE - 1);

		// If M = 0, then 0 coins are required
		dp[0] = 0;

		// Iterate over every coin
		for (int d = 0; d < n; d++) {
			// We start from denominations[d] as when m < denominations[d]
			// We won't be able to add that denomination to required list
			for (int m = denominations[d]; m <= M; m++) {
				dp[m] = Math.min(dp[m], 1 + dp[m - denominations[d]]);
			}
		}

		return dp[M];
	}

	public static void main(String[] args) {
		int coins[] = { 9, 6, 5, 1 };
		int M = 11;
		System.out.println("Minimum coins required is " + minCoins(coins, M));
	}
}
