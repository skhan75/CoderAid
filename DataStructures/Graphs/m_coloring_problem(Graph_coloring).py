# Python program for solution of M Coloring
# problem using backtracking

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]\
                              for row in range(vertices)]

    # A utility function to check if the current color assignment
    # is safe for vertex v
    def isSafe(self, v, colour, c):
        for i in range(self.V):
            # Check for all the "i" neighbors of the current node "v" and
            # check if they have been colored with all the m colors
            # If yes, return False
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    # A recursive utility function to solve m
    # coloring  problem
    def graphColourUtil(self, m, colour, v):
        # If all vertices have been colored, then return true
        if v == self.V:
            return True

        # Else iterate over all colors
        for c in range(1, m+1):
            # If current vertex has a safe color
            if self.isSafe(v, colour, c) == True:
                # Then color the current node
                colour[v] = c
                if self.graphColourUtil(m, colour, v+1) == True:
                    return True
                colour[v] = 0

    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == False:
            return False

        # Print the solution
        print "Solution exist and Following are the assigned colours:"
        for c in colour:
            print c,
        return True

# Driver Code
# Can we color the graph with m colors
g  = Graph(4)
g.graph = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
m=3
g.graphColouring(m)
