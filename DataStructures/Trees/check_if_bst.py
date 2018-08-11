import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_bst(root, min, max):
    if root is None:
        return True

    # Check that the value should be between the upper bound and lower bound range
    if root.data <= min or root.data > max:
        return False

    return is_bst(root.left, min, root.data) and is_bst(root.right, root.data, max)



if __name__ == "__main__":
    INT_MIN = - sys.maxint
    INT_MAX = sys.maxint

    # False
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(15)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)

    print is_bst(root, INT_MIN, INT_MAX)

    # True
    root = Node(10)
    root.left = Node(5)
    root.right = Node(18)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.left.right.right = Node(9)
    root.right.left = Node(15)


    print is_bst(root, INT_MIN, INT_MAX)
