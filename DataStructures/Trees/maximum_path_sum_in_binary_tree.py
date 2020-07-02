"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_path_sum(root):
    # nonlocal max_sum
    def path_sum(node):
        # If no child, return 0
        if node is None:
            return 0

        # 0 to get only positives and ignore negatives
        left = max(0, path_sum(node.left))
        right = max(0, path_sum(node.right))

        # Save the max sum
        path_sum.max_sum = max(path_sum.max_sum, left + right + node.data)

        # Return the max of current sum coming from child nodes
        return max(left, right) + node.data

    # Initialize result
    path_sum.max_sum = float("-inf")
    path_sum(root)
    return path_sum.max_sum


if __name__ == "__main__":
    """
        10
       /  \
      2   10
     / \    \
    20  1   -25
            /  \
           3    4
    """
    root = TreeNode(10)
    root.left = TreeNode(2)
    root.right = TreeNode(10)
    root.left.left = TreeNode(20)
    root.left.right= TreeNode(1)
    root.right.right = TreeNode(-25)
    root.right.right.left = TreeNode(3)
    root.right.right.right = TreeNode(4)


    print max_path_sum(root)
