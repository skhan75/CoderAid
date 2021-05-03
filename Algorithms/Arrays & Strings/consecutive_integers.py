"""
Check if an array is formed by consecutive integers.
You can return the first encountered consecutive series

COMPLEXITY:
    - Runtime: O(N); It can be reduced to O(K) where K < N, by breaking out of the loop
      as soon as you encounter first list of consecutive series
    - Space: O(N)
"""

from collections import defaultdict

def find_consecutive_integers(lst):
    map = defaultdict(list)

    if len(lst) <= 1:
        return None

    # Step is the index pointer pointing to starting point of the next consecutive series
    step = 0
    # Maintain a list of seen elements to avoid duplicates to be considered in the series
    seen = []

    for i in range(1, len(lst)):
        # Append element to the seen
        seen.append(lst[i-1])

        if lst[i] > lst[i-1]:
            if lst[i] not in seen:
                # This step is to basically add the key as the value to itself
                # This is not necessary, but helpful in generating output, by allowing to get the
                # consecutive series from the values
                if not map.get(lst[step]):
                    map[lst[step]].append(lst[step])

                # Append the element in series
                map[lst[step]].append(lst[i])
        else:
            step = i

    # If no series found, return None
    if not map:
        return None

    # Else return the first encountered series list
    return map[list(map.keys())[0]]


import unittest

class Test(unittest.TestCase):

    def test_mixed_bag_1(self):
        test_data = [-1, 5, 4 ,0, 3, 2, 1]
        expected = [-1,5]
        self.assertEqual(find_consecutive_integers(test_data), expected)

    def test_mixed_bag_2(self):
        test_data = [6,4,5,7,8,9,3,2,1]
        expected = [4,5,7,8,9]
        res = find_consecutive_integers(test_data)
        print (res)
        self.assertEqual(res, expected)

    def test_duplicates_1(self):
        test_data = [4,2,4,3,1]
        expected = None
        self.assertEqual(find_consecutive_integers(test_data), expected)

    def test_duplicates_2(self):
        test_data = [5,2,4,5,3,4,1]
        expected = [2,4]
        self.assertEqual(find_consecutive_integers(test_data), expected)


if __name__ == "__main__":
    unittest.main()
