class Graph:

    def __init__(self, is_directed):
        self.all_edges = []
        self.all_vertices = {}
        self.is_directed = is_directed

    def add_edge(self, u_key, v_key, w=0):
        if u_key in self.all_vertices:
            # If there is already a vertex with an associated key
            u_vertex = self.all_vertices[u_key]
        else:
            # Create a new vertex
            u_vertex = Vertex(u_key)
            self.all_vertices[u_key] = u_vertex

        if v_key in self.all_vertices:
            # If there is already a vertex with an associated key
            v_vertex = self.all_vertices[v_key]
        else:
            # Create a new vertex
            v_vertex = Vertex(v_key)
            self.all_vertices[v_key] = v_vertex

        # Create an Edge
        edge = Edge(u_vertex, v_vertex, w, self.is_directed)
        # Add the edge to the list of all edges
        self.all_edges.append(edge)
        # Add the neighboring edges
        u_vertex.add_adjacent_vertices(edge, v_vertex)
        # Add the edge from v_vertex back to u_vertex if it is not directed graph
        if self.is_directed is not True:
            v_vertex.add_adjacent_vertices(edge, u_vertex)

class Edge:

    def __init__(self, u_vertex, v_vertex, weight, is_directed):
        self.u_vertex = u_vertex
        self.v_vertex = v_vertex
        self.is_directed = is_directed
        self.w = weight

    def __eq__(self, other):
        return self.u_vertex.key == other.u_vertex.key and self.v_vertex.key == other.v_vertex.key

    def __hash(self):
        return hash(u_vertex) + hash(v_vertex)

    def __str__(self):
        return "Edge --> " + str(self.u_vertex) + " " + str(self.v_vertex) + " Weight-" + str(self.w)

    def __repr__(self):
        return self.__str__()


class Vertex:

    def __init__(self, key):
        self.key = key
        self.edges = []
        self.adjacent_vertices = []

    def add_adjacent_vertices(self,edge, vertex):
        self.edges.append(edge)
        self.adjacent_vertices.append(vertex)

    def get_degree(self):
        return len(self.edges)

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str("Vertex-" + str(self.key))

    def __repr__(self):
        return self.__str__();

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key


if __name__ == "__main__":
    g = Graph(False)
    g.add_edge(1,2,10)
    g.add_edge(2,3,5)
    g.add_edge(1,4,6)

    print('\nEDGES\n')
    for edge in g.all_edges:
        print(edge)

    print('\nVERTICES')
    for vertex in g.all_vertices:
        print
        print(str(g.all_vertices[vertex]))
        print('Associated Edges')
        for edge in g.all_vertices[vertex].edges:
            print(str(edge))
