 # binary tree node contains data field ,
# left and right pointer
class Node:
    # constructor to create tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lowest_common_ancestor(root, n1, n2):
    # Base Case
    if root is None:
        return

    # Check if root is equal to either of nodes
    if root == n1 or root == n2:
        return root

    # Traverse left subtree to find the node
    left = lowest_common_ancestor(root.left, n1, n2)
    # Traverse right subtree to find the node
    right = lowest_common_ancestor(root.right, n1, n2)

    # if both nodes are found in  left and right subtree
    if left is not None and right is not None:
        # return their common parent
        return root

    # else just get the remaining nodes to search for
    if left is not None:
        return left
    else:
        return right


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

print lowest_common_ancestor(root, root.left.left, root.right.left).data
print lowest_common_ancestor(root, root.left.left, root.left.right).data
