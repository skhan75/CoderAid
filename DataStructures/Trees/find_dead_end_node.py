"""
Given a BST, find a node that has a dead end.
Dead End refers to the node where you cannot insert any more elementself.
Example:       8
             /   \
           5      9
         /   \
        2     7
       /
      1
Here Node 1 is a dead end

Example :     8
            /   \
           7     10
         /      /   \
        2      9     13

Here Node 9 is a dead end
"""

class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def dead_end(root, MIN, MAX):

    if root is None:
        return

    if MIN == MAX:
        return root.key

    return dead_end(root.left, MIN, root.key - 1) or dead_end(root.right, root.key + 1, MAX)

def insert(node, key):

    # If the tree is empty,
    # return a new node
    if node == None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    # return the (unchanged) node pointer
    return node

# Driver Code
if __name__ == "__main__":
    root = None
    root = insert(root, 8)
    root = insert(root, 5)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 7)
    root = insert(root, 11)
    root = insert(root, 4)

    print ("Dead End Node is", dead_end(root, float("-inf"), float("inf")) )
