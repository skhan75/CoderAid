from collections import defaultdict
'''
    For Unidirected fully connected Graph
'''
class Graph:

    def __init__(self):
        # Default dictionary to store graphs
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, source_vertex):
        visited = set()
        self.DFS_Util(source_vertex, visited)

    def DFS_Util(self, vertex, visited):
        visited.add(vertex)
        print(vertex)
        for v in self.graph[vertex]:
            if v not in visited:
                self.DFS_Util(v, visited)


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
#
print ("Following is DFS from (starting from vertex 2)")
g.DFS(2)


'''
    For Unidirected disconnected Graph
'''
class Graph:
    def __init__(self):
        # Default dictionary to store graphs
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS(self):
        print (self.graph)
        V = len(self.graph)
        visited = set()
        vertices = list(self.graph.keys())
        print ('VERTICES', vertices)

        # Call the recursive helper function to print
        # DFS traversal starting from all vertices one
        # by one
        for i in range(V):
            if vertices[i] not in visited:
                self.DFS_Util(vertices[i], visited)

    def DFS_Util(self, vertex, visited):
        visited.add(vertex)
        print(vertex)

        for v in self.graph[vertex]:
            if v not in visited:
                self.DFS_Util(v, visited)

# Driver code
# Create a graph given in the above diagram
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print ("Following is Depth First Traversal")
g.DFS()
