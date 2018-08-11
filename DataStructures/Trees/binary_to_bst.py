# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data  = data
        self.left = None
        self.right = None


def store_inorder_elements(root, array):
    if root is None:
        return

    # First store the left subtree
    store_inorder_elements(root.left, array)
    # Copy the root's data
    array.append(root.data)
    # Finally store the right subtree
    store_inorder_elements(root.right, array)

def copy_array_to_tree(root, array):
    if root is None:
        return

    # Traverse left subtree
    copy_array_to_tree(root.left, array)

    # Copy the value from array to root
    root.data = array[0]
    # Then pop that element
    array.pop(0)

    # Traverse right subtree
    copy_array_to_tree(root.right, array)


# Print the inorder traversal of the tree
def print_inorder(root):
    if root is None:
        return
    print_inorder(root.left)
    print root.data,
    print_inorder(root.right)

def binary_to_bst(root):
    if root is None:
        return

    aux = []
    # 1. Store inorder traversal elements in an auxillary array
    store_inorder_elements(root, aux)

    # 2. Sort the array
    aux.sort()

    # 3. Again traverse in order and copy elements from array into Tree
    copy_array_to_tree(root, aux)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right= Node(5)

    # Convert binary tree to BST
    binary_to_bst(root)

    print "Following is the inorder traversal of the converted BST"
    print_inorder(root)
