class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_bst(root, min, max):
    if root is None:
        return True

    if root.value <= min or root.value > max:
        return False

    if is_bst(root.left, min, root.value) and is_bst(root.right, root.value, max):
        return True

    return False


# Driver Function
INT_MIN = float('-inf')
INT_MAX = float('inf')

root = BinaryTreeNode(10)
root.left = BinaryTreeNode(5)
root.right = BinaryTreeNode(15)
root.left.left = BinaryTreeNode(3)
root.left.right = BinaryTreeNode(8)
root.right.left = BinaryTreeNode(12)
root.right.right = BinaryTreeNode(20)

print is_bst(root, INT_MIN, INT_MAX)
