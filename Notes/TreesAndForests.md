## Counting Trees in a Forest (Graph)
***https://personalpages.manchester.ac.uk/staff/mark.muldoon/Teaching/DiscreteMaths/LectureNotes/TreesAndForests.pdf***

A graph on a vertex set is a collection of unordered pairs of vertices, called edges.

**A Tree is an undirected connected graph without cycles**.
  - That is, there is a path from any vertex to any other, but no path from a vertex to itself that does not traverse each edge on it an even number of times.
  - Without edges, the empty graph has |V| connected components.
  - Each edge that can be added from u --> v creates a path.
  - If there was already a path from u --> v, then it creates a cycle, and then there will be no tree.
  - Otherwise, the new edge joins two previously connected components of the graph to which it is added, into one, and so, after |V|-1 edges are added to the empty graph, we will have  a tree.
  - Thus every tree on n vertices has n-1 edges. We could have  define trees as connected graphs with n-1 edges, or as graphs with n-1 edges without cycles. In other words, any two of the three properties, n-1 edges, connected and no cycles implies the third.
  - **Corollary:** ***A connected graph is a Tree iff all of its edges are bridges.***
  - **Number of Trees:** According to ***Cayleys's Formula*** - There are n ^ (n-2) trees on a vertex set
  V of n elements (isomorphic trees). 

**A Forest is a graph whose connected components are Trees**
 - A forest is a disjoint union of trees, or equivalently an acyclic graph that is not necessarily connected.
 - A forest with k tree components and n nodes has n-k graph edges.

**Counting number of Trees in a Forest**
 - Apply DFS on every node.
 - Increment count by one if every connected node is visited from one source.
 - Again perform DFS traversal if some nodes yet not visited.
 - Count will give the number of trees in forest.
