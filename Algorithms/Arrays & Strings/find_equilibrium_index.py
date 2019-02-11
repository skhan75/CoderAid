"""
Given an array of integers, find the equilibrium index in it
An equilibrium index (i) is one where sum of sub-array A[0...i-1] is equal to the sum of su-array A[i+1...n]

COMPLEXITY: O(n)
"""

def find_equilibrium_index(arr):
    left = [0 for i in range(len(arr))]
    left[0] = 0

    # Iterate from left to right and store the sum of subarray from 0..i-1
    for i in range(1, len(arr)):
        left[i] = left[i-1] + arr[i-1] # ----> n times

    # Now check from right subarray sum that equals to a left subarray sum from left[] list
    # Iterate from n --> i+1
    right = 0
    for i, elem in reversed(list(enumerate(arr))): # ----> k times
        if left[i] == right:
            return arr[i]

        right += elem


import unittest

class Test(unittest.TestCase):

    def test_all_positive_integers_array(self):
        test_data = [1,4,5,2,3,5,8,6,10,4]
        self.assertEqual(find_equilibrium_index(test_data), 8)

    def test_mix_integers_array(self):
        test_data = [1,4,-5,-2,2,5,8,6,-10,-4]
        self.assertEqual(find_equilibrium_index(test_data), 5)


if __name__ == "__main__":
    unittest.main()
