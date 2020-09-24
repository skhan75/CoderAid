class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                # Append neighbor to the Vertex's neighbors list
                self.neighbors.append(neighbor.name)
                # Append the Vertex to the neighbor's neighbors list
                neighbor.neighbors.append(self.name)
                # Sort the  Vertex's neighbors list
                self.neighbors = sorted(self.neighbors)
                # Sort neighbor's neighbors list
                neighbor.neighbors = sorted(neighbor.neighbors)
        else:
            return False

    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            if isinstance(neighbor, Vertex):
                if neighbor.name not in self.neighbors:
                    self.neighbors.append(neighbor.name)
                    neighbor.neighbors.append(self.name)
                    self.neighbors = sorted(self.neighbors)
                    neighbor.neighbors = sorted(neighbor.neighbors)
            else:
                return False

class Graph:
    def __init__(self):
        self.vertices = {}
        self.vertices_nodes = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            self.vertices[vertex.name] = vertex.neighbors
            self.vertices_nodes[vertex] = vertex

    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex, Vertex):
                self.vertices[vertex.name] = vertex.neighbors

    def add_edge(self, from_vertex, to_vertex):
        if isinstance(from_vertex, Vertex) and isinstance(to_vertex, Vertex):
            from_vertex.add_neighbor(to_vertex)
            self.vertices[from_vertex.name] = from_vertex.neighbors
            self.vertices[to_vertex.name] = to_vertex.neighbors

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def bfs(self, source_vertex, Graph):
        # Mark all the vertices as not visited
        visited = set()
        # Create a queue for  bfs
        queue = []
        # Enqueue Source Vertex
        queue.append(source_vertex)
        # Mark it as Visited
        visited.add(source_vertex)
        while queue:
            # Dequeue a vertex from queue and print it
            source = queue.pop(0)
            # Iterate through all the adjacent vertices from the given source
            for vertex in self.vertices[source]:
                # if the vertex is not visited append it the queue and mark it as visted
                if vertex not in visited:
                    queue.append(self.neighbors[vertex])
                    visited.add(vertex)

    def dfs(self, source_vertex):
        vistied = set()
        dfs_util(source_vertex, visited)

    def dfs_util(self, source, visited):
        visited.add(source)

        for vertex in self.vertices[source]:
            if vertex not in visited:
                self.dfs_util(vertex, visited)


    def adjacency_list(self):
        if len(self.vertices) >= 1:
            return [ str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys() ]
        else:
            return dict()

    def adjacency_matrix(self):
        if len(self.vertices) >= 1:
            self.vertex_names = sorted(g.vertices.keys())
            self.vertex_indices = dict(zip(self.vertex_names, range(len(self.vertex_names))))
            import numpy as np
            self.adjacency_matrix = np.zeros(shape=(len(self.vertices),len(self.vertices)))
            for i in range(len(self.vertex_names)):
                for j in range(i, len(self.vertices)):
                    for el in g.vertices[self.vertex_names[i]]:
                        j = g.vertex_indices[el]
                        self.adjacency_matrix[i,j] = 1
            return self.adjacency_matrix
        else:
            return dict()



def graph(g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(g.adjacency_list()) + '\n' + '\n' + str(g.adjacency_matrix())

###################################################################################

a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
e = Vertex('E')

a.add_neighbors([b,c,e])
b.add_neighbors([a,c])
c.add_neighbors([b,d,a,e])
d.add_neighbor(c)
e.add_neighbors([a,c])

g = Graph()
print (graph(g))
g.add_vertices([a,b,c,d,e])
g.add_edge(b,d)
print (graph(g))
# g.bfs(a, g)
