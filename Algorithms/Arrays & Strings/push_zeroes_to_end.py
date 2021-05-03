
def push_zeroes_to_end(arr):

    count = 0 # Count of non-zero elements

    # Traverse the array. If element
    # encountered is non-zero, then
    # replace the element at index
    # 'count' with this element
    for i in range(len(arr)):
        if arr[i] != 0:
            # here count is incremented
            arr[count] = arr[i]
            count+=1

    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end.
    while count < len(arr):
        arr[count] = 0
        count += 1

    return arr
    
import unittest

class Test(unittest.TestCase):

    def test_zeroes_to_end(self):
        test_data = [5,1,0,1,0,0,0,2,5,7,0,9,1]
        expected = [5,1,1,2,5,7,9,1,0,0,0,0,0]
        self.assertEqual(push_zeroes_to_end(test_data), expected)

if __name__ == "__main__":
    unittest.main()
