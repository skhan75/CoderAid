class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_second_largest(root):
    if root is None:
        return

    # We've reached the rightmost which doesn't have a right child,
    # so we traverse left and find the subsequent rightmost second largest child
    if root.left is not None and root.right is None:
        return find_second_largest(root.left)

    # We found the parent of the second largest
    if root.right is not None and root.right.left is None and root.right.right is None:
        return root.data

    # Otherwise keep going right
    return find_second_largest(root.right)


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(8)
root.right.left = Node(12)
root.right.right = Node(20)

print find_second_largest(root)
