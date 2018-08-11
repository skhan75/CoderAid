def remove_duplicates(input):
    unique = ''
    for ch in input:
        if ch not in unique:
            unique += ch
    del input
    return unique


import unittest
class Test(unittest.TestCase):
    def test_remove_duplicates(self):
        #true check
        data_1 = ['hello', '123123', 'fire']
        expected_1 = ['helo', '123', 'fire']

        i = 0
        for test_string in data_1:
            res = remove_duplicates(test_string)
            self.assertEqual(res, expected_1[i])
            i += 1


if __name__ == "__main__":
    unittest.main()
