"""
Given an array of stock prices, find the buy and sell pairs that can give maximum profitself.

COMPLEXITY:
    - Runtime: O(n) 
"""

def get_max_buy_sell_pairs(stock_prices, n):

    # Find the local maxima (denoting selling price) and local minima (denoting buying price)
    local_maxima = []
    local_minima = []

    i = 0
    while i < n-1:
        # Get the Local Minima
        if stock_prices[i] < stock_prices[i+1]:
            local_minima.append(stock_prices[i])

        # Don't go in looking for local_maxima until you find a local_minima
        else:
            i += 1
            continue

        # Finding local maxima
        flag = True
        j = i+1

        while flag and j < n-1:

            if stock_prices[j] >= stock_prices[j+1]:
                local_maxima.append(stock_prices[j])
                i = j
                flag = False

            elif j == n-2:
                local_maxima.append(stock_prices[j+1])
                i = j
                flag = False

            j+=1

        i += 1

    return construct_max_pairs(local_minima, local_maxima)



def construct_max_pairs(l1, l2):
    pairs = []
    for i in range(len(l1)):
        pairs.append(( l1[i], l2[i] ))

    return pairs



import unittest

class Test(unittest.TestCase):

    def test_1(self):
        test_data = [100, 180, 260, 310, 40, 535, 695]
        expected = [(100, 310), (40, 695)]
        self.assertEqual(get_max_buy_sell_pairs(test_data, len(test_data)), expected)

    def test_1(self):
        test_data = [200, 180, 260, 310, 40, 535, 695]
        expected = [(180, 310), (40, 695)]
        self.assertEqual(get_max_buy_sell_pairs(test_data, len(test_data)), expected)


if __name__ == "__main__":
    unittest.main()
