# binary tree node contains data field ,
# left and right pointer
class Node:
    # constructor to create tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# function to print all path from root
# to leaf in binary tree
def print_paths(root):
    # list to store path
    path = []
    print_inorderly(root, path)

# Does a recursive inorder traversal to print all the paths
def print_inorderly(root, path):

    # Base condition
    if root is None:
        return

    # add current root's data into list
    path.append(root.data)

    # Keep traversing left subtree
    print_inorderly(root.left, path)

    # Till you find the leaf node
    if root.left is None and root.right is None:
        # leaf node then print the list
        print_array(path)

    # Traverse right
    print_inorderly(root.right, path)

    # Once you print the leaf node and backtrack, pop the leaf node from the list
    path.pop()

# Helper function to print list in which
# root-to-leaf path is stored
def print_array(ints):
    for i in ints:
        print i," ",
    print ''

# Driver program to test above function
"""
Constructed binary tree is
            10
            / \
          8     2
         / \   /
        3   5 2
"""
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

print_paths(root)
