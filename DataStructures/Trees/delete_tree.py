class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def delete_tree(root):

    if root is None:
        return


    #Post order traversal
    delete_tree(root.left)
    delete_tree(root.right)

    # Then delete the node
    print ('Deleting Node ', root.data)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    delete_tree(root)
    root = None
