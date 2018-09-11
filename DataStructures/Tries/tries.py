class TrieNode:

    def __init__(self):
        self.children = {}#[None]*26 # Since 26 alphabets
        self.end_of_word = False


class Trie:

    def __init__(self):
        # Assign a new TrieNode as the root
        self.root = TrieNode()

    def insert(self, word):
        # Assign root as the current
        current = self.root

        # Iterate through characters in the word
        for char in word:

            # If character is not in current's children
            if char not in current.children:
                # create a node
                node = TrieNode()
                # Add node as children to current
                current.children[char] = node

            # Incrementing Current
            current = current.children[char]

        # Initializing end of word indicating a complete word
        current.end_of_word = True


    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False
            else:
                node = current.children[char]

            current = node

        return current.end_of_word




t = Trie()

t.insert('hello')
t.insert('hell')
t.insert('hel')
print t.search('hel') # True
print t.search('hello') # True
print t.search('he') # False
