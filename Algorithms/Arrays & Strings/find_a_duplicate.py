""" INTERVIEW CAKE
Find a duplicate, Space Edition.

We have a list of integers, where:

The integers are in the range 1..n1..n
The list has a length of n+1n+1
It follows that our list has at least one integer which appears at least twice.
But it may have several duplicates, and each duplicate may appear more than twice.

Write a function which finds an integer that appears more than once in our list.
(If there are multiple duplicates, you only need to find one of them.)

We're going to run this function on our new, super-hip MacBook Pro With Retina Display.
Thing is, the damn thing came with the RAM soldered right to the motherboard,
so we can't upgrade our RAM. So we need to optimize for space!
"""

import unittest

def find_repear(list):

    # Initialize left and right bounds
    left, right = 1, len(list)-1

    while left < right:

        # Using the Binary Search approach to divide the list into
        # left and right ranges, such that they don't overlap
        # and then use the sub structures to find an element that doesn't belong
        # to the range

        mid = left + (left-right) // 2

        # Dividing the list into lower and upper ranges
        # with their left and right bounds
        lower_left, lower_right = left, mid
        upper_left, upper_right = mid+1, right

        # Keeping count of items that should belong to lower range
        items_in_lower_range = 0

        for item in list:
            # Incrementing the count whenever we find such item
            if item >= lower_left and item <= lower_right:
                items_in_lower_range += 1


        # Possible items that should be in the lower range
        distinct_possible_items_in_lower_range = lower_right - lower_left + 1

        if items_in_lower_range > distinct_possible_items_in_lower_range:
            # There must be a duplicate in the lower range
            left, right = lower_left, lower_right
        else:
             # There must be a duplicate in the upper range
             left, right = upper_left, upper_right



    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor




# Driver Function

class Test(unittest.TestCase):

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)
