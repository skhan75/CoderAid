class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level(root, node, lvl):

    # Base case
    if root is None:
        return False

    if root == node:
        return lvl

    # Search in left subtree
    left = level(root.left, node, lvl+1)
    # If node is found, return the level from left
    if left != 0:
        return left
    # Else Search in right subtree
    return level(root.right, node, lvl+1)

def is_sibling(root, n1, n2):
    # Base case
    if root is None:
        return 0

    return ((root.left == n1 and root.right == n2) or
            (root.left == n2 and root.right == 1) or
            is_sibling(root.left, n1, n2) or
            is_sibling(root.right, n1, n2))

def is_cousin(root, n1, n2):
    if (level(root, n1, 1) == level(root, n2, 1)) and not (is_sibling(root, n1, n2)):
        return 1

    return 0



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(15)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)

    node1 = root.left.right.right
    node2 = root.right

    print "Yes" if is_cousin(root, node1, node2) == 1 else "No"
