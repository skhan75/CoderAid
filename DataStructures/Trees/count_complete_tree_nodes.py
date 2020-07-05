"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def countNodes(root):
    if root is None:
        return 0

    left_levels = 1
    left_node = root.left

    while left_node:
        left_node = left_node.left
        left_levels += 1

    right_levels = 1
    right_node = root.right

    while right_node:
        right_node = right_node.right
        right_levels += 1

    if left_levels == right_levels:
        return 2**left_levels - 1

    return 1 + countNodes(root.left)  + countNodes(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.right.left = Node(6)
    root.right.right = Node(6)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)

    print countNodes(root)
