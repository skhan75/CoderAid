"""
Given a tree of n nodes, remove the maximum number of edges from this tree such
that each connected component of the resultant forest has an even number of vertices.

APPROACH:
---------
 - Initialize a variable edges_to_remove counter as 0
 - Traverse the connected components from a source, and count the no of components during the traversal
   when you trace back. (DFS)
 - The moment you count reaches an even no, increment the counter edges_to_remove by 1.
 - Repeat the algorithm until you have covered all the nodes.
"""

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, root, visited, edges_to_remove):
        # This is the count for all the connected components associated with the root node
        connected_component_counts = 0
        # This is the count for the current nodes during the iteration of the depth
        current_iteration_count = 0

        # Add all the visited nodes to the set
        visited.add(root)

        # Explore the nodes of the root
        for v in self.graph[root]:
            if v not in visited:

                # Recur through other connected nodes from the same source
                current_iteration_count = self.dfs(v, visited, edges_to_remove)

                # Whenever the iteration count becomes even
                # We know, we found our even sub tree, so we can increment connected_component_counts by 1
                # This is the count when our recursive stack is pointing to the even node
                # But we need to back track again one more time till we find an odd node count.
                # This is the node from where the break will happen
                if current_iteration_count%2:
                    connected_component_counts += current_iteration_count
                # Else when reached an odd node we add 1 to the final answer denoting the count
                else:
                    edges_to_remove[0] += 1

        return connected_component_counts + 1

    def convert_tree_to_forest(self):
        edges_to_remove = [0]
        visited = set()

        root_node = list(self.graph.keys())[0]

        self.dfs(root_node, visited, edges_to_remove)

        return edges_to_remove[0]


import unittest
class Test(unittest.TestCase):

    def test_1(self):
        edges = [(1,3), (1,6), (1,2), (3,4), (6,8), (2,7), (2,5), (4,9), (4,10)]
        g = Graph()

        for edge in edges:
            g.add_edge(edge[0], edge[1])

        res = g.convert_tree_to_forest()
        self.assertEqual(res, 2)

    def test_2(self):
        edges = [(0,1), (0,2), (0,3), (1,4), (1,5), (4,15), (4,16), (2,8), (2,9), (9,11), (9,12), (3,6), (6,7)]
        g = Graph()

        for edge in edges:
            g.add_edge(edge[0], edge[1])

        res = g.convert_tree_to_forest()
        self.assertEqual(res, 1)

    def test_no_edges_can_be_removed(self):
        edges = [(0,1), (0,2), (0,3)]
        g = Graph()

        for edge in edges:
            g.add_edge(edge[0], edge[1])

        res = g.convert_tree_to_forest()
        self.assertEqual(res, 0)


if __name__ == "__main__":
    unittest.main()
