"""
Check if a Sub array with sum 0 exists or not

For finding a subarray with a subset sum which equals to a given sum, refer "DynamicProgramming/subset_sum"
Complexity: O(n)

Logic:
------

For optimal runtime, we use hashing to keep a track of the sum as we move forward in the array.
    - Iterate from 0 --> n in the array
    - Keep calculating sum for the iterations and put them in a hashset.
    - We have a subarray that sums out to 0:
        - if the sum repeats itself (i.e. if its already present in the hashset)
        - or if the sum becomes 0
        - or if there's a 0 in array
"""

def has_subbarray_0_sum(arr):
    s = set()

    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if (sum in s) or (sum is 0):
            return True

        s.add(sum)

    return False


import unittest
class Test(unittest.TestCase):

    def test_has_subbarray_0_sum(self):
        data_true = [[4, 2, -3, 1, 6], [4, 2, 0, 1, 6], [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]]

        for test in data_true:
            res = has_subbarray_0_sum(test)
            self.assertTrue(res)

        data_false = [[-3, 2, 3, 1, 6], [1, 2, 3, 4, 5, 6]]
        for test in data_false:
            res = has_subbarray_0_sum(test)
            self.assertFalse(res)

if __name__ == "__main__":
    unittest.main()
