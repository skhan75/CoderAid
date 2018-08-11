class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class ReverseTree:

    def __init__(self):
        self.list = []


    def reverse_util(self, root, target, path):

        if root is None:
            return

        path.append(root.data)

        if root.data == target:
            print path
            self.list = path
            return

        else:
            self.reverse_util(root.left, target, path)
            self.reverse_util(root.right, target, path)



    def reverse_tree_path(self, root, target):
        # temp = {}
        self.reverse_util(root, target, [])
        print self.list

# Print the inorder traversal of the tree
def print_inorder(root):
    if root is None:
        return
    print_inorder(root.left)
    print root.data,
    print_inorder(root.right)



root = Node(7)
root.left = Node(6)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(3)
root.right.left= Node(2)
root.right.right= Node(1)

# print_inorder(root)
rt = ReverseTree()
rt.reverse_tree_path(root, 6)

# print_inorder(root)
