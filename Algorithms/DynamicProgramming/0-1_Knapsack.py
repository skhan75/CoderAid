"""
Problem Statement
=================
0/1 Knapsack Problem - Given items of certain weights/values and maximum allowed weight how to pick items to pick items
from this set to maximize sum of value of items such that sum of weights is less than or equal to maximum allowed
weight.
Runtime Analysis
----------------
Time complexity - O(W*total items)
Video
-----
* Topdown DP - https://youtu.be/149WSzQ4E1g
* Bottomup DP - https://youtu.be/8LusJS5-AGo
References
----------
* http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/
* https://en.wikipedia.org/wiki/Knapsack_problem
"""
import numpy as np

def knapsack_01(values, weights, total_weight):
    total_items = len(weights)

    # rows will contain all the items
    rows = total_items + 1
    # cols will contain weights in increasing order from 0 to total_weight
    cols = total_weight + 1

    T = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            # If tot weight j is less than weight at i
            if j < weights[i-1]:
                # Take the value from above
                T[i][j] = T[i-1][j]
            else:
                # Max of best weight coming from top (i.e. if we do not select
                # current value) and Selecting value of current weight + remaining weight
                T[i][j] = max(T[i-1][j], values[i-1] + T[i-1][j - weights[i-1]])

    print np.matrix(T)
    return T[rows-1][cols-1]


if __name__ == '__main__':
    total_weight = 7
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    expected = 9
    assert expected == knapsack_01(values, weights, total_weight)
    total_weight = 8
    weights = [2, 2, 4, 5]
    values = [2, 4, 6, 9]
    expected = 13
    assert expected == knapsack_01(values, weights, total_weight)
