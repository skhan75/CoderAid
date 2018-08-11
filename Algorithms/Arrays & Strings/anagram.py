def remove_duplicates(s):
    unique = ''
    for ch in s:
        if ch not in s:
            unique += ch
    del s
    return unique

def is_anagram(s1, s2):
    s1, s2 = remove_duplicates(s1), remove_duplicates(s2)
    if s1 == s2:
        return True
    else:
        return False

import unittest

class Test(unittest.TestCase):
    def test_anagram(self):
        #true case
        data_1 = [('man', 'nam'), ('silent', 'listen')]
        for test_string in data_1:
            res = is_anagram(test_string[0], test_string[1])
            self.assertTrue(res)

        #false case
        data_2 = [('boy', 'toy'), ('happy', 'happiness')]
        for test_string in data_2:
            res = is_anagram(test_string[0], test_string[1])
            self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
