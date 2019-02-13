""" Check if a given array can represent Preorder Traversal of Binary Search Tree """

def can_represent_bst(array):

    # Create an Empty stack
    s = []

    # Initialize current root as minimum possible value
    root = float("-inf")

    # Traverse given array
    for value in array:
        # If we find out a node on the right hand side which is smaller than
        # the root, return False
        if value < root:
            return False

        # Keep removing items smaller than value and make the last removed
        # item as the new root
        while len(s) > 0 and s[-1] < value:
            root = s.pop()

        # At this point either stack is empty or value
        # is smaller than root, push value
        s.append(value)

    return True



if __name__ == "__main__":
    input = [51, 41, 45, 81, 111]
    print (can_represent_bst(input))
