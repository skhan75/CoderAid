"""
Given keys from 1 to n, construct all possible BSTs.
If we take a closer look, we can notice that the count is basically n’th Catalan numbers.

COMPLEXITY: O(2^n!) 
"""
class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def construct_possible_bsts(start,end):
    solution = []

    # Base Case: Reached out of bounds - if this happens, then it means no bst is formed
    if start > end:
        solution.append(None)
        return solution

    # Exploring possibilities for creating left and right subtrees
    for i in range(start, end+1):

        # Constructing Left Subtree
        left_subtree = construct_possible_bsts(start, i-1)

        # Constructing Right Subtree
        right_subtree = construct_possible_bsts(i+1, end)

        # Now constuct all bsts for ith node as the root and combinations from
        # left subtree and right subtree and append each combination to solution
        for j in range(len(left_subtree)):
            left = left_subtree[j]
            for k in range(len(right_subtree)):
                right = right_subtree[k]
                root = Node(i)
                root.left = left
                root.right = right
                solution.append(root)

    return solution

def print_preorder(root):

    if root is None:
        return

    print (root.key, end=' ')
    print_preorder(root.left)
    print_preorder(root.right)




import unittest

class Test(unittest.TestCase):

    def testing_varying_n_values(self):
        test_data = [3,5,8,10]

        for t in test_data:
            solution = construct_possible_bsts(1, t)
            print('No of BSTs when n is', t, 'is', len(solution))
            for bst in solution:
                print_preorder(bst)
                print()


if __name__ == "__main__":
    unittest.main()
