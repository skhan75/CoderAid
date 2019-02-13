# Python program to find the inroder successor in a BST

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def inOrderSuccessor(root, data):

    # Search the Node -- O(h)
    current = find(root, data)

    if current == None:
        return None

    # Case-1 When Node has a right subtree
    if current.right != None:
        temp = current.right

        while temp.left is not None:
            temp = temp.left

        return temp

    # Case-2 When Node has no right subtree
    successor = None
    ancestor = root

    while ancestor != current:
        if current.data < ancestor.data:
            successor = ancestor
            ancestor = ancestor.left
        else:
            ancestor = ancestor.right

    return successor



def find(root, data):
    if root is None:
        return None

    if root.data == data:
        return root

    elif root.data < data:
        return find(root.right, data)

    else:
        return find(root.left, data)



# Given a non-empty binary search tree, return the
# minimum data value found in that tree. Note that the
# entire tree doesn't need to be searched
def minValue(node):
    current = node

    # loop down to find the leftmost leaf
    while(current is not None):
        if current.left is None:
            break
        current = current.left

    return current


# Given a binary search tree and a number, inserts a
# new node with the given number in the correct place
# in the tree. Returns the new root pointer which the
# caller should then use( the standard trick to avoid
# using reference parameters)
def insert( node, data):

    # 1) If tree is empty then return a new singly node
    if node is None:
        return Node(data)
    else:

        # 2) Otherwise, recur down the tree
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node

        # return  the unchanged node pointer
        return node


# Driver progam to test above function

root  = None

# Creating the tree given in the above diagram
root = insert(root, 20)
root = insert(root, 8);
root = insert(root, 22);
root = insert(root, 4);
root = insert(root, 12);
root = insert(root, 10);
root = insert(root, 14);
succ_of = root.left.right.right

succ = inOrderSuccessor( root, succ_of.data)
if succ is not None:
    print ("\nInorder Successor of %d is %d " \
            %(succ_of.data , succ.data))
else:
    print ("\nInorder Successor doesn't exist")
