class TreeNode:

    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def has_children(self):
        return self.left_child or self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def has_both_children(self):
        return self.left_child and self.right_child


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def insert(self, value):
        if self.root:
            self._insert(value, self.root)
        else:
            self.root = TreeNode(value)
        self.size += 1

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.has_left_child():
                self._insert(value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(value, parent=current_node)
        else:
            if current_node.has_right_child():
                self._insert(value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(value, parent=current_node)

    def search(self, value):
        res = self._get(value, self.root)
        if res:
            return True
        else:
            return False

    def _get(self, value, current_node):
        if current_node is None:
            return None
        elif current_node.value == value:
            return current_node
        elif value < current_node.value:
            return self._get(value, current_node.left_child)
        else:
            return self._get(value, current_node.right_child)

    def __contains__(self,value):
        if self._get(value, self.root):
            return True
        else:
            return False

    def delete(self, value):
        if self.size > 1:
            node_to_remove = self._get(value, self.root)
            if node_to_remove:
                removed = self.remove(node_to_remove)
                self.size -= 1
                return removed
            else:
                raise ValueError('Element not in Tree')
        elif self.size == 1 and self.root.value == value:
            self.root = None
            self.size -= 1
        else:
            raise ValueError('Element not in Tree')
        return

    def remove(self, node_to_remove):
        if node_to_remove.has_right_child():
            replacer = self.find_successor(node_to_remove)
            
            if replacer.has_right_child():
                replacer.parent.left_child = replacer.right_child

            replacer.right_child = node_to_remove.right_child
            if node_to_remove.has_left_child():
                replacer.left_child = node_to_remove.left_child

        elif node_to_remove.has_left_child():
            replacer = self.find_predecessor(node_to_remove)

            if replacer.has_left_child():
                replacer.parent.right_child = replacer.left_child

            replacer.left_child = node_to_remove.left_child
            if node_to_remove.has_right_child():
                replacer.right_child = node_to_remove.right_child

        removed = node_to_remove
        node_to_remove = None

        return removed

    def find_successor(self, node):
        successor = None
        if node.has_right_child():
            successor = self.find_min(node.right_child)
        return successor

    def find_predecessor(self, node):
        predecessor = None
        print (node.value)
        if node.has_left_child():
            predecessor = self.find_max(node.left_child)
        return predecessor

    def find_min(self, node):
        min_node = None
        if node.has_left_child():
            min_node = find_min(node.left_child)
        else:
            min_node = node
        return min_node

    def find_max(self, node):
        max_node = None
        if node.right_child:
            max_node = find_max(node.right_child)
        else:
            max_node = node
        return max_node



if  __name__ == "__main__":
    B = BinarySearchTree()
    B.insert(6)
    B.insert(3)
    B.insert(7)
    B.insert(2)
    B.insert(4)
    B.insert(10)
    B.insert(9)
    print(B.search(4))
    print('ANSWER',B.delete(3))
    print(B.search(3))
