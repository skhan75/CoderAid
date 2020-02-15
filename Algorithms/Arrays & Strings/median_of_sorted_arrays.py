"""
There are two sorted arrays X and Y of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""

import unittest

def avg(a,b):
    return (a+b) / 2

def find_median_of_two_arrays(x, y):
    # Pick the smaller array as the first array
    if len(x) > len(y):
        x, y = y, x

    m, n = len(x), len(y)
    MIN, MAX = float("-inf"), float("inf")

    # Now we need to find two partitions such that,
    # both partitions have equal no. of elements
    # i.e. partition_x + partition_y = m+n+1 / 2
    low, high = 0, m
    elements_in_a_partition = (m+n+1) // 2
    is_even = True if (m+n)%2 == 0 else False

    # We use Binary Search to find such partitions
    while low <= high:
        partition_x = (low+high) // 2
        partition_y = elements_in_a_partition - partition_x # partition_x + partition_y = m+n+1 / 2

        # Partition X is 0 if there is nothing on the left side and Partition X is m if there is nothing on the right
        max_left_x = MIN if partition_x == 0 else x[partition_x - 1]
        min_right_x = MAX if partition_x == m else x[partition_x]

        max_left_y = MIN if partition_y == 0 else y[partition_y - 1]
        min_right_y = MAX if partition_y == n else  y[partition_y]

        # Condition - 1: Condition when a perfect match is FOUND, this is the median
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if is_even:
                return avg(max(max_left_x, max_left_y), min(min_right_x, min_right_y))
            else:
                return max(max_left_x, max_left_y)

        # Condition - 2: When our pivot is too much on the right, we move our pivot on partition_x toward left
        elif max_left_x > min_right_y:
            high = partition_x - 1

        # Condition - 3: When our pivot is too much on the left, we move our pivot towards right
        else:
            low = partition_x + 1



class Test(unittest.TestCase):
    def test_simple(self):
        actual = find_median_of_two_arrays([1,2],[3, 4])
        expected = 2.5
        self.assertEqual(actual, expected)

    def test_second_array_smaller(self):
        actual = find_median_of_two_arrays([1,3],[2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_odd(self):
        actual = find_median_of_two_arrays([1,3,5,8,9],[7,11,18,19,21,25])
        expected = 9
        self.assertEqual(actual, expected)

    def test_even(self):
        actual = find_median_of_two_arrays([1,3,5,6,8,9],[7,11,18,19,21,25])
        expected = 8.5
        self.assertEqual(actual, expected)

    def test_with_empty_array_1(self):
        actual = find_median_of_two_arrays([],[7,11,18,19,21,25])
        expected = 18.5
        self.assertEqual(actual, expected)

    def test_with_empty_array_2(self):
        actual = find_median_of_two_arrays([2],[])
        expected = 2
        self.assertEqual(actual, expected)


if __name__ == "__main__":
	unittest.main()
