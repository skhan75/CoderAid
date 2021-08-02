class BuySellStockProfit3 { // With 2 transactions allowed

	/*
	* Space Complexity -- O(N)
	* Time --> O(N)
	*/
	public int maxProfitBidirectionalApproach(int[]  prices) {
		int N = prices.length;

		if(N <= 1) return 0;

		int leftMin = prices[0];
		int rightMax = prices[N-1];

		int[] leftProfits = new int[N];
		int[] rightProfits = new int[N+1];

		for(int l=1; l<N; ++l) {

			leftProfits[l] = Math.max(leftProfits[l-1], prices[l] - leftMin);
			leftMin = Math.min(leftMin, prices[l]);

			int r = N-1-l;

			rightProfits[r] = Math.max(rightProfits[r+1], rightMax - prices[r]);
			rightMax = Math.max(rightMax, prices[r]);
		}

		int maxProfit = 0;
		for(int i=0; i<N; ++i) {
			maxProfit = Math.max(maxProfit, leftProfits[i] + rightProfits[i+1]);
		}

		return maxProfit;

	}


	public int maxProfit(int[] prices) {
		// 4 variables
		// t1_buy --> Buy transaction#1 
		// t1_profit --> Sell trasnaction#1 

		// t2_buy --> Buy transaction2 MIN(t2_buy, price - t1_profit)
		// t2_profit --> Sell transaction2

		int t1_buy = Integer.MAX_VALUE;
		int t2_buy = Integer.MAX_VALUE;

		int t1_profit = 0;
		int t2_profit = 0;

		for(int price : prices) {

			// Select the first minimum buy price
			t1_buy = Math.min(t1_buy, price);
			t1_profit = Math.max(t1_profit, price - t1_buy);

			// Use the remaining cash from 1 maximum profit transaction and using it for second transactio
			t2_buy = Math.min(t2_buy, price - t1_profit);
			t2_profit = Math.max(t2_profit, price - t2_buy);
		}

		return t2_profit;
	}


	public static void main(String[] args) {
		BuySellStockProfit3 bs = new BuySellStockProfit3();
		int[] prices1 = {7,1,5,3,6,4};
		int[] prices2 = {3,3,5,0,0,3,1,4};
		System.out.println("Max profit "+bs.maxProfitBidirectionalApproach(prices1));
		System.out.println("Max profit "+bs.maxProfitBidirectionalApproach(prices2));

		System.out.println("Max profit "+bs.maxProfit(prices1));
		System.out.println("Max profit "+bs.maxProfit(prices2));
	}
}