# Disjoint Set Forest Representation: (Faster Implementation)
#
#
# Runitime Complexity:
#   n, total no of elements
#   m, total no of MAKE_SET, UNION and FIND_SET operations
#
#   The no of UNION operation is atmost n-1.
#   Since, MAKE_SET operations are included in the total number of operations m,
#   we have m >= n
#
#   O(m alpha(n)), where alpha(n) is a slow growing function.
#   alpha(n) <= 4.
#   Therefore, complexity becomes O(4m), which is equivalent to O(m)

class Node:
    def __init__(self, data, parent=None, rank=0):
        # Data is used to store the data
        self.data = data
        # Parent is the pointer from chiuld to parent
        self.parent = parent
        # Rank is used to store the approximate depth of the tree
        self.rank = rank

    def __str__(self):
        return str(self.data)

class DisjointSet:
    def __init__(self):
        self.map = {}

    def make_set(self, data):
        node = Node(data)
        node.parent = node
        self.map[data] = node

    def union(self, data1, data2):
        node1 = self.map[data1]
        node2 = self.map[data2]

        parent1 = self.find_set_util(node1)
        parent2 = self.find_set_util(node2)

        # If the parent are same, do nothing
        if parent1.data == parent2.data:
            return

        if parent1.rank > parent2.rank:
            parent2.parent = parent1
        elif parent1.rank < parent2.rank:
            parent1.parent = parent2
        else:
            parent2.parent = parent1
            parent1.rank += 1

    def find_set(self, data):
        return self.find_set_util(self.map[data])

    def find_set_util(self, node):
        parent = node.parent

        # Parent always point itself as the parent.
        # Hence the only way you break out of recursion is when find a cycle
        # i.e. parent pointing 'parent' as itself
        if parent == node:
            return parent

        node.parent = self.find_set_util(node.parent)

        return node.parent

if __name__ == '__main__':
    ds = DisjointSet()
    ds.make_set(1)
    ds.make_set(2)
    ds.make_set(3)
    ds.make_set(4)
    ds.make_set(5)
    ds.make_set(6)
    ds.make_set(7)

    ds.union(1,2)
    ds.union(2,3)
    ds.union(4,5)
    ds.union(6,7)
    ds.union(5,6)
    ds.union(3,7)

    for i in range(1,8):
        print(ds.find_set(i))
