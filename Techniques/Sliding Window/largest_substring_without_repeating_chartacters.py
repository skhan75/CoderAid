"""
Given a string, find the length of the longest substring without repeating characters.
"""

import unittest

"""
APPROACH - 1
Complexity: O(2n)
Runtime: 65 ms, faster than 45.40% of Python online submissions for Longest Substring Without Repeating Characters.
"""
def length_of_longest_substring(s):
	pivot, slider, ans = 0,0,0
	lookup_table = set()

	n = len(s)
	while slider<n:
		if s[slider] not in lookup_table:
			lookup_table.add(s[slider])
			slider += 1
			ans = max(len(lookup_table), ans)
		else:
			lookup_table.remove(s[pivot])
			pivot += 1
		

	return ans		

"""
APPROACH - 2
Complexity - O(n)
Runtime: 56 ms, faster than 76.50% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""
def length_of_longest_substring_optim(s):
	i, ans,n = 0, 0, len(s)
	table = {}

	for j in range(n):
		if s[j] in table.keys():
			i = max(table[s[j]], i)

		ans = max(ans, j-i+1)
		table[s[j]] = j+1

	return ans





class Test(unittest.TestCase):
	def test_approach_1(self):
		actual1 = length_of_longest_substring("abcabcbb")
		self.assertEqual(actual1, 3)

		actual2 = length_of_longest_substring("pwwwkew")
		self.assertEqual(actual2, 3)

		actual3 = length_of_longest_substring("tmmzuxt")
		self.assertEqual(actual3, 5)
		
	def test_approach_2(self):
		actual1 = length_of_longest_substring_optim("abcabcbb")
		self.assertEqual(actual1, 3)

		actual2 = length_of_longest_substring_optim("pwwwkew")
		self.assertEqual(actual2, 3)

		actual3 = length_of_longest_substring_optim("tmmzuxt")
		self.assertEqual(actual3, 5)
	# def test_medium_string(self):
	# def test_long_string(self):

if __name__ == "__main__":
	unittest.main(argv=['first-arg-is-ignored'], exit=False)