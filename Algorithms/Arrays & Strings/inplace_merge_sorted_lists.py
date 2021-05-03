"""
Given two sorted arrays, merge them in-placeself.
The conversion should be done in place without uising any additional data structures.
"""







import unittest

class Test(unittest.TestCase):
    #
    [1,4,10,22]
    [3,7,11,13,21,25,30,31]

    # [1,2,7,10,13,22]
    # [3,4,8,11,14,21,25,31]

    def test_two_non_empty_lists(self):
        actual = merge_lists([1,2,8,10,13,22], [3,4,7,11,14,21,25,31])
        # self.assertEqual([1,2,3,4,8,10,11,13,14,21,22,31])

if __name__ == "__main__":
    unittest.main()
