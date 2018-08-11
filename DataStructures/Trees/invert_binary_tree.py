class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def invert(root):
    if not root:
        return

    # Iterate left subtree
    invert(root.left)
    # Iterate right subtree
    invert(root.right)

    # Swap Nodes
    temp = root.left
    root.left = root.right
    root.right = temp


# Print the inorder traversal of the tree
def print_inorder(root):
    if root is None:
        return
    print_inorder(root.left)
    print root.data,
    print_inorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


print_inorder(root)
print('')

invert(root)

print_inorder(root)
