from collections import defaultdict
from DisjointSets import *

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_dfs_util(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                if self.is_cyclic_dfs_util(i, visited, v):
                    return True
            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif parent != i:
                return True
        return False

    def is_cyclic_dfs(self):
        visited = [False] * self.V
        for i in range(self.V):
            if visited[i] == False:
                if self.is_cyclic_dfs_util(i, visited, -1) == True:
                    return True
        return False

    def is_cyclic_bfs(self):
        visited = [False] * (self.V + 1)
        queue = []
        parents = [-1] * (self.V + 1)
        source  = self.graph.keys()[0]
        queue.append(source)
        visited[source] = True

        while queue:
            s = queue.pop(0)
            # Explore all the neighbors of s
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    parents[i] = s
                elif parents[i] != s:
                    return True
        return False

    def is_cyclic_disjoint_set(self):
        disjoint_set = DisjointSet()
        for data in range(self.V):
            disjoint_set.make_set(data)

        parent = [-1]*self.V
        for u in self.graph:
            for v in self.graph[u]:
                # Finding parent for u
                x = disjoint_set.find_set(u).data
                # Finding parent for v
                y = disjoint_set.find_set(v).data
                if x == y:
                    return True
                else:
                    disjoint_set.union(u, v)
        return False

# Create a graph given in the above diagram
g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)


if g.is_cyclic_bfs():
    print "Graph contains cycle"
else :
    print "Graph does not contain cycle "
if g.is_cyclic_dfs():
    print "Graph contains cycle"
else :
    print "Graph does not contain cycle "

if g.is_cyclic_disjoint_set():
    print "Graph contains cycle"
else :
    print "Graph does not contain cycle "
