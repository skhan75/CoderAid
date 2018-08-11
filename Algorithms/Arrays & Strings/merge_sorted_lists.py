import unittest


def merge_lists(first_list, second_list):
    
    merged_list_size = len(first_list) + len(second_list)
    merged_list = [None] * merged_list_size

    current_index_first_list = 0
    current_index_second_list = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:

        is_first_list_exhausted = current_index_first_list >= len(first_list)
        is_second_list_exhausted = current_index_second_list >= len(second_list)

        if not is_first_list_exhausted and ( is_second_list_exhausted or
            first_list[current_index_first_list] < second_list[current_index_second_list]):

            # Merge from first list
            merged_list[current_index_merged] = first_list[current_index_first_list]

            current_index_first_list += 1

        else:

            # Merge from second list
            merged_list[current_index_merged] = second_list[current_index_second_list]

            current_index_second_list += 1


        current_index_merged += 1

    return merged_list





# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
