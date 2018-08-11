class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Complexity --> O(n)
def print_level_order_traversal(root):

    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue root and initialize height
    queue.append(root)

    while len(queue) > 0:
        print queue[0].data,
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


# Complexity --> O(n)
def print_level_order_traversal_linebyline(root):
    print('\n')

    # Base Case
    if root is None:
        return

    # Initialize an empty Queue
    queue = []

    # Append the root to the queue
    queue.append(root)

    while True:
        # Keep track of count of nodes in a level
        nodes_count_at_a_level = len(queue)

        if nodes_count_at_a_level == 0:
            break

        # Traverse by nodes count at a level
        while nodes_count_at_a_level > 0:
            # Print the data at a level
            print queue[0].data,
            # Pop the element from end of the queue
            current_node = queue.pop(0)

            # Append its childs to the queue for subsequent levels
            if current_node.left is not None:
                queue.append(current_node.left)

            if current_node.right is not None:
                queue.append(current_node.right)

            nodes_count_at_a_level -= 1

        print '\n'



#Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(6)
root.left.right = Node(5)

print 'Simple Level Order Traversal'
print_level_order_traversal(root)
print '\n\nLevel Order Traversal Line By Line'
print_level_order_traversal_linebyline(root)
