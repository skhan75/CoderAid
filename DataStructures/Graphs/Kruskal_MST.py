# Runtime Complexity Analysis:
#   1. Sorting Edges by weight --> O(E lg E)
#   2. There are O(E) FIND_SET and UNION operations from line 49-61
#   3. O(V) MAKE_SET operation
#   4. No of edges is greater than or equal to V-1, Hence for each edge, we do (2) and (3),
#   causing the total of O((V+E) alpha(V))
#   where, alpha(V) is a slow growing (log) function due to Union using path compression.
#   5. We assume that G (graph) is connected, hence we have E >= V - 1
#   6. So, Disjoint Set operation takes O(E alpha(V)) time.
#   7. Moreover, alpha(V) = O(lg E) = O(lg V)
#
#   Hence, total Runtime is : **  O(E lg V) **

from DisjointSets import *
from collections import defaultdict

#Class to represent a graph
class Graph:

   def __init__(self,vertices):
       self.V= vertices #No. of vertices
       self.graph = [] # default dictionary to store graph

   # function to add an edge to graph
   def addEdge(self,u,v,w):
       self.graph.append([u,v,w])

   # The main function to construct MST using Kruskal's
       # algorithm
   def KruskalMST(self):
       disjoint_set = DisjointSet()

       result =[] #This will store the resultant MST

       i = 0 # An index variable, used for sorted edges
       e = 0 # An index variable, used for result[]

       # Step 1:
       # Sort all the edges in non-decreasing order of their
       # weight. If we are not allowed to change the
       # given graph, we can create a copy of graph
       self.graph =  sorted(self.graph,key=lambda item: item[2])

       # Create V subsets with single elements -- Make Set
       for node in range(self.V):
           disjoint_set.make_set(node)


       # Number of edges to be taken is equal to V-1
       #
       # While e is less than total no of vertices
       while e < self.V -1 :

           # Step 2: Pick the smallest edge and increment
           # the index for next iteration
           u,v,w =  self.graph[i]
           i = i + 1
           x = disjoint_set.find_set(u).data
           y = disjoint_set.find_set(v).data

           # Skipping cycles
           if x == y:
               continue

           # Else append non cyclic edge to results
           # And perform union on two set of nodes
           else:
               e = e+1
               result.append([u,v,w])
               disjoint_set.union(x,y)

       # print the contents of result[] to display the built MST
       print "Following are the edges in the constructed MST"
       for u,v,weight  in result:
           #print str(u) + " -- " + str(v) + " == " + str(weight)
           print ("%d -- %d == %d" % (u,v,weight))

# Driver code
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMST()
