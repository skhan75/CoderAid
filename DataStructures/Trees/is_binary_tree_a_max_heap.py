class BTNode:
    '''A generic binary tree node.'''

    def __init__(self, v):
        '''(BTNode, int) -> NoneType

        Initialize a new BTNode with value v.

        '''
        self.value = v
        self.left = None
        self.right = None


def is_max_heap(node):
    '''(BTNode) -> bool

    Return True iff the binary tree rooted at node is a max-heap
    Precondition: the tree is complete.

    '''
    if node.left and node.right is None:
        return True
    else:
        if node.value > node.left.value and node.value > node.right.value:
            return is_max_heap(node.left) and is_max_heap(node.right)
        else:
            return False


if __name__ == '__main__':
    l1 = BTNode(7)
    l2 = BTNode(6)
    l3 = BTNode(8)
    l1.left = l2
    l1.right = l3
    print(is_max_heap(l1))
