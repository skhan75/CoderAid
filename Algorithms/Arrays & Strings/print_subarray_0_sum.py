"""
Given an array of integers, print all subarrays with 0 sum
"""
from collections import defaultdict

def print_subarrays_with_0_sum(arr):
    s = defaultdict(list)
    s[0].append(-1)
    solution = []

    sum = 0
    for i in range(len(arr)):
        sum += arr[i]

        if (sum in s):
            # find all sub-arrays with same sum
            lst = s[sum]
            for val in lst:
                solution.append((val+1, i))

        s[sum].append(i)

    return solution


import unittest

class Test(unittest.TestCase):

    def test_print_subarrays_with_0_sum(self):

        test_data = [[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]]
        expected = [ [(0, 2), (1, 3), (2, 5), (5, 7), (0, 9), (3, 9)] ]
        for idx, t in enumerate(test_data):
            res = print_subarrays_with_0_sum(t)
            self.assertEqual(res, expected[idx])


if __name__ == "__main__":
    unittest.main()
