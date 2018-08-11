# prices --> list of stock values over len(prices) days
# k --> no of transactions allowed
def max_profit_slow_solution(prices, k):
    if k == 0 or prices == []:
        return 0

    days = len(prices)
    num_transactions = k + 1 # including 0th transaction

    # Let T be our solution matrix
    T = [[0 for _ in range(days)] for _ in range(num_transactions)]

    # We are starting from 1 because we will be filling column at day 0th
    # with zeroes since no matter how many transactions you have if you have price for
    # just 1 day, you cannot make any profit.
    # Similarly, we have filled the 0th row with all zeroes, because
    # no matter how many days you have, if you have 0 transaction, you don't
    # make any profit
    for transaction in range(1, num_transactions):
        for day in range(1, days):
            # This maximum value is either:
            # 1. Max from previous day transaction
            # 2. Max profit made by selling on the day plus cost of
            # previous transaction considered over m days
            T[transaction][day] = max(T[transaction][day-1],
                                    max([
                                        (prices[day] - prices[m] + T[transaction-1][m])
                                        for m in range(day)
                                    ])
                                )


    print_actual_solution(T, prices)

    # Return last value in the matrix
    return T[-1][-1]


def print_actual_solution(T, prices):
    transaction = len(T) - 1
    day = len(T[0]) - 1
    stack = []

    while True:
        if transaction == 0 or day == 0:
            break

        if T[transaction][day] == T[transaction][day-1]:
            # This mean we didn't sell anything
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
    # assert 10 == max_profit_optimized(prices, 3)
    # print ('\n')
    assert 10 == max_profit_slow_solution(prices, 3)
