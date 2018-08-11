import unittest


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome

    unpaired_character = set()

    for char in the_string:

        # Check for all pairs
        if char in unpaired_character:
            unpaired_character.remove(char)

        else:
            unpaired_character.add(char)

    # The string has a palindrome permutation
    # if it has 1 or 0 character without a pair
    return len(unpaired_character) <= 1


# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
