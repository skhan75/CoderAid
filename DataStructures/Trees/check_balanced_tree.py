def is_balanced(root_node):
    if root_node is None:
        return True

    left_height = height(root_node.left)
    right_height = height(root_node.right)

    height_diff = abs(right_height - left_height)

    if height_diff <= 1 and is_balanced(root_node.left) and is_balanced(root_node.right):
        return True

    return False


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


if __name__ == "__main__":
    print (is_balanced(root_node))
