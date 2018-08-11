"""
Writing programming interview questions hasn't made me rich yet ...
so I might give up and start trading Apple stocks all day instead.

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the
best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.
"""

"""EXAMPLE:
stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)
"""

""" BRUTE FORCE APPROACH: Complexity --> O(n^2)
    ------------------------------------------
     try every pair of times (treating the earlier time as the buy time and
     the later time as the sell time) and see which one is higher.
"""
def get_max_profit_brute_force(stock_prices):
    max_profit = 0

    # Go through every time with index (indx, value)
    for earlier_time, earlier_price in enumerate(stock_prices):

        # And go through all the later prices
        for later_time in xrange(earlier_time+1, len(stock_prices)):

            later_price = stock_prices[later_time]

            # Now we calculate the potential profit if we bought at earlier price and
            # sell at later_price
            potential_profit = later_price - earlier_price

            # Update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit


""" OPTIMIZED SOLUTION: Complexity --> O(n) [Greedy], Space --> O(1)
    -------------------
    The max profit we get is simply the difference we get from the current price and the min of
    a value in earlier time.
    So for every price we need to:
                - keep track of the lowest prices we've seen so far
                - see if we can get any better profit
"""
def get_max_profit_optimized(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires atleast 2 prices')

    # We'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices[0]
    # Handling negative cases by doing so
    max_profit = stock_prices[1] - stock_prices[0]

    # We should start at the second index, since we have to buy the first time
    # in order to sell it and we can't buy and sell at the same time
    for current_time in xrange(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        potential_profit = current_price - min_price

        # Update the max_profit
        max_profit = max(max_profit, potential_profit)

        # Update the min_price
        min_price = min(min_price, current_price)


    return max_profit


print get_max_profit_brute_force([10, 7, 5, 8, 11, 9])
print get_max_profit_optimized([10, 7, 5, 8, 11, 9])
