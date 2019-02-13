"""
Convert a BST to Min Heap

ALGORITHM:
    - Create an auxillary array of size n
    - Perform Inorder traversal on the BST and copy the node values to the auxillary array list
    - Now perform the Preorder traversal of the tree
    - While traversing the root during pre order traversal copy the values from the array to the node

COMPLEXITY:
    - Runtime: O(n)
    - Space: O(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root, aux):
    if root is None:
        return

    inorder_traversal(root.left, aux)
    aux.append(root.data)
    inorder_traversal(root.right, aux)

def preorder_traversal(root, aux, i):
    if root is None:
        return

    i[0] += 1
    root.data = aux[i[0]]

    preorder_traversal(root.left, aux, i)
    preorder_traversal(root.right, aux, i)


def bst_to_min_heap(node):
    aux = []
    i = [-1]

    inorder_traversal(node, aux)

    # Pre Order will basically put all the items in the aux array into
    # right places in the tree while traversing it, by putting first the element and
    # then traversing left and right
    preorder_traversal(node, aux, i)


# function for the preorder traversal
# of the tree
def print_tree(root):
    if root is None:
        return

    # first print the root's data
    print(root.data, end = " ")

    # then recur on left subtree
    print_tree(root.left)

    # now recur on right subtree
    print_tree(root.right)

# Driver Code
if __name__ == '__main__':

    # BST formation
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    bst_to_min_heap(root)
    print("Preorder Traversal:")
    print_tree(root)
