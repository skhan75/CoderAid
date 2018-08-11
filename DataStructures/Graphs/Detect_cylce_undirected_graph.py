from collections import defaultdict
from DisjointSets import *

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic(self):
        disjoint_set = DisjointSet()

        for data in range(self.V):
            disjoint_set.make_set(data)

        parent = [-1]*self.V

        for u in self.graph:
            for v in self.graph[u]:
                # Finding parent for u
                x = disjoint_set.find_set(u).data
                print 'x',x
                # Finding parent for v
                y = disjoint_set.find_set(v).data
                print 'y',y

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

if g.is_cyclic():
    print "Graph contains cycle"
else :
    print "Graph does not contain cycle "
