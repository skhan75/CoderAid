"""
Problem Statement:
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Time Complexity:
1. Recursive Solution = O(2^n)
2. Dynamic Programming Solution = O(n^2)

"""


def max_profit_dp(prices, rod_length):
    # This is the optimal cut of rod length up until i
    rod_length_vals = [0 for _ in range(rod_length+1)]

    for length in range(1, rod_length+1):
        max_val = float('-inf')

        # Each cut length
        for cut_length in range(1, length+1):
            # prices[cut_length] is the price at a particular cut_length
            max_val = max(max_val, prices[cut_length-1] + rod_length_vals[length-cut_length])

        rod_length_vals[length] = max_val

    return rod_length_vals[rod_length]



if __name__ == '__main__':
    prices = [3,5,8,9,10,20,22,25]
    rod_length = 8
    expected_max_profit = 26
    assert expected_max_profit == max_profit_dp(prices, rod_length)
