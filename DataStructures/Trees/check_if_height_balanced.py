# A binary tree Node
class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1


def is_balanced(root):

    if root is None:
        return

    lh = height(root.left)
    rh = height(root.right)

    if abs(lh - rh) <=1 and is_balanced(root.left) is True and is_balanced(root.right) is True:
        return True

    return False


# Driver function to test the above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
if is_balanced(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")
