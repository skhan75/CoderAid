class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        # Assign root as the current
        current = self.root

        # Iterate through characters in the word
        for char in word:
            # create a node
            node = TrieNode()
            # If character is not in current's children
            if char not in current.children:
                # Add node as children to current
                current.children[char] = node

            # Incrementing Current
            current = node

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
print t.search('hell')
