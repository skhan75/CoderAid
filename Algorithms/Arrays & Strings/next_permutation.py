"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Courtesy @ LeetCode
"""

def swap(nums, i, j):
    print i, j, nums
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

def reverse(nums, beg, end):
    while beg < end:
        swap(nums, beg, end)
        beg += 1
        end -= 1


def next_permutation(nums):
    if len(nums) == 1:
        return
    if len(nums) == 2:
        return swap(nums, 0, 1)

    # Start from second last element
    dec = len(nums) - 2

    # Find a point from reverse where the ascending order ends, that is the point which gives the lagest number possible
    while dec >= 0 and nums[dec] >= nums[dec + 1]:
        dec -= 1

    # Now reverse that largest possible sub digits
    reverse(nums, dec + 1, len(nums) - 1)

    if dec == -1:
        return nums

    # Now find the immediate next digit which is greater than dec
    next_num = dec + 1
    while next_num < len(nums) and nums[next_num] <= nums[dec]:
        next_num+=1

    # Swap the digits
    swap(nums, next_num, dec)

    return nums
    

import unittest
class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = next_permutation([1,2,3])
        self.assertEqual(result, [1,3,2])

    def test_permutation_with_even_number_of_chars(self):
        result = next_permutation([3,2,1])
        self.assertEqual(result, [1,2,3])

    def test_no_permutation_with_odd_number_of_chars(self):
        result = next_permutation([1,1,5])
        self.assertEqual(result, [1,5,1])

    def test_no_permutation_with_even_number_of_chars(self):
        result = next_permutation([5,4,3,2,1])
        self.assertEqual(result, [1,2,3,4,5])

    def test_empty_string(self):
        result = next_permutation([1,2,7,9,6,4,1])
        self.assertEqual(result, [1,2,9,1,4,6,7])



unittest.main(verbosity=2)
