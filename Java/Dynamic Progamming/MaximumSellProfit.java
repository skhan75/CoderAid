public class MaximumSellProfit {

	/*
		Time Complexity --> O(N) for N daily prices
		Space Complexity --> O(N) for N-1 memoizations
	*/
	public int maxProfitTopDown(int[] dailyPrices) {
		int lastDay = dailyPrices.length - 1;
		boolean noStock = false; 

		return getBestProfit(lastDay, noStock, dailyPrices);
	}

	private int getBestProfit(int day, boolean noStock, int[] dailyPrices) {
		int strategyBuy=0, strategySell=0, strategyHold=0, strategyAvoid=0;
		
		// Base case 
		if(day < 0) {
			// if no stock, 0 profit
			if(noStock) {
				return 0;	
			} else { // else return negative, as we are not allowed to have initial stock
				return Integer.MIN_VALUE;
			}
		}

		int currentPrice = dailyPrices[day];

		// We can reach this state, by buying or holding
		if(noStock) {
			strategyBuy = getBestProfit(day-1, false, dailyPrices) - currentPrice; // buying the stock, so we now we own it and have less money
			strategyHold = getBestProfit(day-1, true, dailyPrices); // holding the stock so that we keep our money unchanged
		} else {
			strategySell = getBestProfit(day-1, true, dailyPrices) + currentPrice; // selling the stock, so we no longer own it and have more money
			strategyAvoid = getBestProfit(day-1, false, dailyPrices); // Avoiding the stock so we keep our money unchanged
		}

		return Math.max(strategySell, strategyAvoid);
	}


	/*
		Time Complexity --> O(N) for N daily prices
		Space Complexity --> O(1) since we are only storing the result from the previous day
	*/
	public int maxProfitBottomUp(int[] dailyPrices) {

		// Initial State: start from a reference cash amount
		int cashAvailable = 0; 

		// High penality for owning a cash initially
		int cashAcquired = Integer.MIN_VALUE;

		for(int price : dailyPrices) {

			int strategyBuy = cashAvailable - price; 
			int strategyHold = cashAcquired;

			int strategySell = cashAcquired + price; 
			int strategyAvoid = cashAvailable;

			cashAcquired = Math.max(strategyBuy, strategyHold);
			cashAvailable = Math.max(strategySell, strategyAvoid);
		}

		// We return the maximum cash available after consecutive sequences of buy and sell to incur maximum profit
		// Max Profit = Cash Available in the end
		return cashAvailable;
	}

	public static void main(String[] args) {
		MaximumSellProfit msp = new MaximumSellProfit();

		int[] dailyPrices = {2,5,1,3};
		System.out.println("Maximum Profit acquired by selling stocks is "+msp.maxProfitTopDown(dailyPrices));
		System.out.println("Maximum Profit acquired by selling stocks is "+msp.maxProfitBottomUp(dailyPrices));
	}
}