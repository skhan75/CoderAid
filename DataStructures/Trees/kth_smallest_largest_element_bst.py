"""
Finding the Kth largest and Kth smallest element in a BST

LOGIC:
    - Do a Reverse In Order Traversal for kth largest
    - And a Regular In Order Traversal for kth smallest
    - And when count == k, stop and return the element
"""

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

def kth_largest_element(root, k, count):

    if root is None or count[0] >= k:
        return

    # We'll make use of recursion's call stack to reach the rightmost end of the BST
    # Recur for Right Subtree
    kth_largest_element(root.right, k, count)

    # Now we trace back from the call stack --> pointing to the rightmost element in BST
    # Increment the counter
    count[0] += 1

    # If count equals k, we have found our kth largest element
    if count[0] == k:
        print ("Kth Largest element is ", root.key)
        return

    # Now Recur for Left Sub Tree
    kth_largest_element(root.left, k, count)

def kth_smallest_element(root, k, count):

    if root is None or count[0] >= k:
        return

    # For finding the Kth smallest, we'll just do the opposite
    # We'll do a regular In Order traversal
    kth_smallest_element(root.left, k, count)

    count[0] += 1

    if count[0] == k:
        print ("Kth Smallest element is ", root.key)
        return

    # now recur for right subtree
    kth_smallest_element(root.right, k, count)


def insert(node, key):

    # If the tree is empty,
    # return a new node
    if node == None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    # return the (unchanged) node pointer
    return node


# Driver code
if __name__ == '__main__':

    # Let us create following BST
    #        50
    #      /    \
    #     30    70
    #    /  \  /  \
    #   20 40 60 80
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    k = 2

    kth_largest_element(root, 2, [0])
    kth_smallest_element(root, 2, [0])
