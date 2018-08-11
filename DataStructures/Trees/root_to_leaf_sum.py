# binary tree node contains data field ,
# left and right pointer
class Node:
    # constructor to create tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_path_with_sum(root, sum, results):
    if root is None:
        return

    if root.left is None and root.right is None:
        if root.data == sum:
            results.append(root.data)
            return True
        else:
            return False

    if check_path_with_sum(root.left, sum - root.data, results):
        results.append(root.data)
        return True

    if check_path_with_sum(root.right, sum - root.data, results):
        results.append(root.data)
        return True

    return False



# Driver program to test above function
"""
Constructed binary tree is
            10
            / \
          8     2
         / \   /
        3   5 2
"""
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

print check_path_with_sum(root, 23, [])
print check_path_with_sum(root, 11, [])
