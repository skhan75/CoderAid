
# A Binary Tree Node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def construct_tree(pre, size):

    # The first element is always the root
    root = Node(pre[0])

    s = []

    # Push root
    s.append(root)

    # Iterate through the rest of the array
    for value in pre[1:]:

        temp = None

        # Keep on popping while next value is greater than stack's top value
        while len(s) > 0 and value > s[-1].data:
            temp = s.pop()

        # If temp is not Null, that means the value is greater than root
        # and hence should be its right child
        if temp is not None:
            temp.right = Node(value)
            s.append(temp.right)

        # Else it should be the left child of the current root
        else:
            temp = s[-1]
            temp.left = Node(value)
            s.append(temp.left)

    return root

def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print root.data,
    printInorder(root.right)



if __name__ == "__main__":
    pre = [10, 5, 1, 7, 40, 50]
    root = construct_tree(pre, len(pre))
    print root.right.data
    printInorder(root)
