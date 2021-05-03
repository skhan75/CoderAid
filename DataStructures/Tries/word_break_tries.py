"""
PROBLEM: Word Break
Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung"
or "i like sam sung".
"""

"""
Optimized Approach - Using Tries Datastructure:
-----------------------------------------------

Complexity:
-----------
    - Insert and search costs O(n), where n is the length of the word
    - Space Complexity is O(nN), where,
            n is length of word
            N is no of words in the Trie
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.string = None


class Trie:

    def insert(self, word, root):
        current = root

        for char in word:
            if char not in current.children:
                node = TrieNode()
                current.children[char] = node
            current = current.children[char]

        current.end_of_word = True


    def search(self, root, key):
        current = root

        # Iterate for all characters in the key string
        for char in key:
            # If character not found in the current's children list
            # That means that substring is not in the list.
            if char not in current.children:
                return False

            current = current.children[char]

        return current.end_of_word;

    def word_break(self, str, root):
        size = len(str)

        # Base Case - If size is zero, that means we have traversed and check the whole string with True.
        # Hence return True
        if size == 0:
            return True

        # Try for all the prefixes of lengths from 1 to size
        for i in range(1, size+1):
            # Search for the substring and recurse the same for all substrings
            if self.search(root, str[0:i]) is True and self.word_break(str[i: size+1], root):
                return True

        # If we have exhausted all the prefixes, we'll return False
        return False



dictionary = [
    "mobile","samsung","sam","sung",
    "man","mango","icecream","and",
    "go","i","like","ice","cream"
]

trie = Trie()

root = TrieNode()

# Insert all the words from the dictionary into the Trie
for word in dictionary:
    trie.insert(word, root)

assert trie.word_break("ilikesamsung", root) == True
assert trie.word_break("iiiiiiii", root) == True
assert trie.word_break("",root) == True
assert trie.word_break("samsungandmango",root) == True
assert trie.word_break("samsungandmangok",root) == False
