"""
Given n nodes of a forest (collection of trees), find the number of trees in the forest.

APPROACH :
1. Apply DFS on every node.
2. Increment count by one if every connected node is visited from one source.
3. Again perform DFS traversal if some nodes yet not visited.
4. Count will give the number of trees in forest.

COMPLEXITY:
 - Runtime: O(V+E)
"""
#Python program to print topological sorting of a DAG
from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def count_trees(self):
        visited = set()
        vertices = list(self.graph.keys())
        count = 0

        for i in range(len(self.graph)):
            if vertices[i] not in visited:
                self.dfs_util(vertices[i], visited)
                count += 1

        return count

    def dfs_util(self, vertex, visited):
        visited.add(vertex)

        for v in self.graph[vertex]:
            if v not in visited:
                self.dfs_util(v, visited)


import unittest
class Test(unittest.TestCase):

    def test_1(self):
        edges = [(0,1), (0,2), (3,4)]
        g = Graph()

        for edge in edges:
            g.add_edge(edge[0], edge[1])

        res = g.count_trees()
        self.assertEqual(res, 2)




if __name__ == "__main__":
    unittest.main()
