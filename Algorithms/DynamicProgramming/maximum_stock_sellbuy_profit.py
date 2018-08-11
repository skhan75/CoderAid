""""
Problem Statement:
Given certain stock values over a period of days (d days) and a number K,
the number of transactions allowed, find the maximum profit that be obtained
with at most K transactions.

Complexity:
* Space Complexity O(days * transctions)
* Time Complexity: Slow Solution O (days^2 * transactions), Faster Solution O(days * transaction)
"""

# prices --> list of stock values over len(prices) days
# k --> no of transactions allowed
def max_profit_slow_solution(prices, k):
    if k == 0 or prices == []:
        return 0

    days = len(prices)
    num_transactions = k+1 # 0th transaction up to and including kth transaction is considered.

    # let T be our solution matrix
    T = [[0 for _ in range(days)] for _ in range(num_transactions)]

    # We are starting from 1 because we have filled all the column at row 0 with 0s,
    # since if the transaction is 0, then it doesn't matter what the prices are, profit will
    # always be 0
    for transaction in range(1, num_transactions):
        # same as above for the days, no matter how many transactions you have, the profit
        # for same day is always gonna be 0
        for day in range(1, days):
            # This maximum value of either:
            # 1. max from previous day transaction
            # 2. Max profit made by selling on the day plus the cost of the previous transaction,
            #    considered over m days
            T[transaction][day] = max(T[transaction][day-1],
                                        max([
                                            (prices[day] - prices[m] + T[transaction-1][m])
                                            for m in range(day)
                                        ])
                                    )

    print_actual_solution(T, prices)

    # Return last value on the matrix
    return T[-1][-1]


def max_profit_optimized(prices, k):
    if k == 0 or prices == []:
        return 0

    days = len(prices)
    num_transactions = k+1 # 0th transaction up to and including kth transaction is considered.

    T = [[0 for _ in range(days)] for _ in range(num_transactions)]

    for transaction in range(1, num_transactions):
        # initial max_diff = 0 - prices[0]
        max_diff = -prices[0]

        for day in range(1, days):
            T[transaction][day] = max(T[transaction][day-1], # No transaction
                                     prices[day] + max_diff) # price on that day with max diff
            max_diff = max(max_diff, T[transaction-1][day] - prices[day])

    print_actual_solution(T, prices)

    # Return last value on the matrix
    return T[-1][-1]


def print_actual_solution(T, prices):
    transaction = len(T) - 1
    day = len(T[0]) - 1
    stack = []

    while True:
        if transaction == 0 or day == 0:
            break

        if T[transaction][day] == T[transaction][day-1]: # This mean we didn't sell anything
            # so go a row above or a day back
            day -= 1

        else: # This means transaction took place
            stack.append(day)  # Sold
            max_diff = T[transaction][day] - prices[day]

            # Now we are gonna look a row above (transaction above)
            # to find a day which gives the remaining price(max_diff)
            for k in range(day-1, -1, -1):
                if T[transaction-1][k] - prices[k] == max_diff:
                    stack.append(k) # Bought
                    transaction -= 1
                    break

    for entry in range(len(stack) - 1, -1, -2):
        print("Buy on day {day} at price {price}".format(day=stack[entry], price=prices[stack[transaction]]))
        print("Sell on day {day} at price {price}".format(day=stack[entry], price=prices[stack[transaction - 1]]))




if __name__ == '__main__':
    prices = [2, 5, 7, 1, 4, 3, 1, 3]
    assert 10 == max_profit_optimized(prices, 3)
    print ('\n')
    assert 10 == max_profit_slow_solution(prices, 3)
