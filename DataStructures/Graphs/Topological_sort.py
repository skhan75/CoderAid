#Python program to print topological sorting of a DAG
from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        visited = set()
        stack = []
        vertices = self.graph.keys()

        for i in range(len(self.graph)):
            if vertices[i] not in visited:
                self.topological_sort_Util(vertices[i], visited, stack)

        print (stack)

    def topological_sort_Util(self, vertex, visited, stack):
        visited.add(vertex)

        for v in self.graph[vertex]:
            if v not in visited:
                self.topological_sort_Util(v, visited, stack)

        stack.insert(0, vertex)
        print stack

g = Graph()
g.add_edge(5, 2);
g.add_edge(5, 0);
g.add_edge(4, 0);
g.add_edge(4, 1);
g.add_edge(2, 3);
g.add_edge(3, 1);

print ("Following is a Topological Sort of the given graph")
g.topological_sort()
