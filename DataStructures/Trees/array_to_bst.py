class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sorted_array_to_bst(array):
    if not array:
        return None

    # Find middle
    mid = len(array) / 2

    # make the middle element as the root
    root = Node(array[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = sorted_array_to_bst(array[:mid])

    # right subtree of root has all
    # values > arr[mid]
    root.right = sorted_array_to_bst(array[mid+1:])

    return root

# A utility function to print the preorder
# traversal of the BST
def print_preorder(root):
    if not root:
        return

    print root.data,
    print_preorder(root.left)
    print_preorder(root.right)

def array_to_bst(array):
    # Sort the array (O(nlogn))
    array.sort()
    # Find the middle as root and assign left and right (O(n))
    return sorted_array_to_bst(array)


if __name__ == "__main__":
    input = [10, 5, 8, 3, 2, 15, 12, 20]
    root = array_to_bst(input)
    print_preorder(root)
