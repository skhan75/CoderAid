# Method 1 : Using SET data structure
def unique_string_1(input):
    s = set(input)
    if len(s) < len(input):
        print 'not unique'
    else:
        print 'unique'

# Method 2: Without Data structure
def unique_string_2(s):
    char_set = [False for _ in range(128)]
    flag = True

    for i in range(0, len(s)):
        ascii_val = ord(s[i])
        if char_set[ascii_val] is not True:
            char_set[ascii_val] = True
        else:
            flag = False
            break

    if flag is True:
        return True
    else:
        return False
       

import unittest
class Test(unittest.TestCase):
    data_1 = ["sami", "earth", ""]
    data_2 = ["hello", "3211asfa ()", "2412421124", "%$%%#^&*"]
    
    def test_unique(self):
        #true check
        for test_string in self.data_1:
            actual = unique_string_2(test_string)
            self.assertTrue(actual)
        #false check
        for test_string in self.data_2:
            actual = unique_string_2(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    #input = raw_input().strip()
    #unique_string_1(input)
    #unique_string_2(input)
    unittest.main()
