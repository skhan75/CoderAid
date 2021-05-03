"""
We can find a mother vertex in O(V+E) time.
The idea is based on Kosaraju’s Strongly Connected Component Algorithm.
In a graph of strongly connected components, mother vertices are always vertices
of source component in component graph. The idea is based on below fact.

If there exist mother vertex (or vertices),
then one of the mother vertices is the last finished vertex in DFS.
(Or a mother vertex has the maximum finish time in DFS traversal).
"""


# program to find a mother vertex in O(V+E) time
from collections import defaultdict

# This class represents a directed graph using adjacency list
# representation
class Graph:

    def __init__(self,vertices):
        self.V = vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary

    # A recursive function to print DFS starting from v
    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # Add w to the list of v
    def addEdge(self, v, w):
        self.graph[v].append(w)

    # Returns a mother vertex if exists. Otherwise returns -1
    def findMother(self):

        # visited[] is used for DFS. Initially all are
        # initialized as not visited
        visited =[False]*(self.V)

        # To store last finished vertex (or mother vertex)
        v=0

        # Do a DFS traversal and find the last finished
        # vertex
        for i in range(self.V):
            if visited[i]==False:
                self.DFSUtil(i,visited)
                v = i

        # If there exist mother vertex (or vetices) in given
        # graph, then v must be one (or one of them)

        # Now check if v is actually a mother vertex (or graph
        # has a mother vertex). We basically check if every vertex
        # is reachable from v or not.

        # Reset all values in visited[] as false and do
        # DFS beginning from v to check if all vertices are
        # reachable from it or not.
        visited = [False]*(self.V)
        self.DFSUtil(v, visited)
        if any(i == False for i in visited):
            return -1
        else:
            return v

# Create a graph given in the above diagram
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(5, 2)
g.addEdge(6, 0)
print "A mother vertex is " + str(g.findMother())
