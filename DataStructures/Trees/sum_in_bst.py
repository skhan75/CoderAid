""" BST to a Tree with sum of all smaller keys """

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class SumTree:
    def __init__(self):
        self.add_val = 0

    def sum_util(self, root):
        if root is None:
            return

        self.sum_util(root.left)

        self.add_val += root.data
        root.data = self.add_val

        self.sum_util(root.right)



    def sum_in_bst(self, root):
        self.sum_util(root)
        return root


# Print the inorder traversal of the tree
def print_inorder(root):
    if root is None:
        return
    print_inorder(root.left)
    print root.data,
    print_inorder(root.right)

if __name__ == "__main__":
    root = Node(9)
    root.left = Node(6)
    root.right = Node(15)
    root.left.left = Node(3)
    root.right.right= Node(21)

    print "Before Sum"
    print_inorder(root)

    tree = SumTree()

    tree.sum_in_bst(root)

    print "\n\nAfter Sum"
    print_inorder(root)
