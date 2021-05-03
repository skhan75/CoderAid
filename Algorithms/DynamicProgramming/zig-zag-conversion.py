"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
"""
import unittest

def convert(s, numRows):
    i, j = 0, 0
    goDown = True

    result = [[] for i in range(numRows)]

    if numRows == 1 or numRows == len(s):
        return s

    while j < len(s):
        if i==numRows-1:
            goDown = False

        if i==0:
            goDown = True

        result[i].append(s[j])

        if goDown is True:
            i+=1

        else:
            i-=1

        j+=1


    batch = []
    for r in result:
        batch.append("".join(r))

    return "".join(batch)


class Test(unittest.TestCase):
    def test_simple(self):
        actual = convert("PAYPALISHIRING", 4)
        expected = "PINALSIGYAHRPI"
        self.assertEqual(actual, expected)

    def test_short_string(self):
        actual = convert("AB", 1)
        expected = "AB"
        self.assertEqual(actual, expected)

    def test_equal_rows_and_string(self):
        actual = convert("PAYPALISHIRING", 14)
        expected = "PAYPALISHIRING"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
