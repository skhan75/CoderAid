def is_substring(s1, s2):
    if len(s1) == len(s2) != 0:
        s1 += s1
        if s2 in s1:
            return True
    return False



import unittest
class Test(unittest.TestCase):
    def test_is_substring(self):
        # true case
        data_1 = [('waterbottle', 'erbottlewat'), ('electronics', 'ctronicsele'), ("1234", "3412")]
        for test_string in data_1:
            res = is_substring(test_string[0], test_string[1])
            self.assertTrue(res)
        # false case
        data_2= [('foo', 'foofoo'), ('happy', 'sad'), ("1234", "5432")]
        for test_string in data_2:
            res = is_substring(test_string[0], test_string[1])
            self.assertFalse(res)
if __name__ == "__main__":
    unittest.main()
