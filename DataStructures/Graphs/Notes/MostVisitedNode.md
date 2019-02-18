## Most Visited Node in a Graph
#### References:
1. https://www.topcoder.com/community/competitive-programming/tutorials/range-minimum-query-and-lowest-common-ancestor/#Range_Minimum_Query_(RMQ)

2. https://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/


This is a very classic example of FOF (Friends of Friends) type of implementation where you want to find the most ranked mutual connection among all the connections.

#### Example

Given N nodes, connected by exactly N-1 edges (there is exactly 1 shortest path from one node to any other node) and Q queries, which tell source node and the destination nodes.

For example, Q queries are:

```
1 5
2 4
3 1
```

So travel from node 1 to node 5, then from node 2 to node 4, then from node 3 to node 1. Finally, find what is the most visited node after the Q queries.

#### Analysis

**Naive Approach:**

Now in this type of problem, a very naive approach would be to find every path and increment every visited node count.
 - We can traverse every node using BFS or DFS in O(V+E)
 - And we have to do this every time for each query, so O(Q x (V+E)), which makes sense and in simpler terms would be a possible solution for interview based questions.
 - But now lets try to complicate this a little further. Imagine you have a system where you are getting Queries (Q) in real time (most of them happening concurrently) and your Graph is very large.
 - Now if we tend to process the same information i.e. traversing the Graph and finding most visited node, again and again for all those Q queries, you may have an non-efficient runtime and may be exhausting your memory. This is a very bad approach in that case.

 **Optimization:**

 Optimizations always comes with a tradeoff, depending on what we are trying to optimize.
 Here in our case, it seems like we have redundancy in terms of time and processing, but we can have ample of space to store the pre-processed meta information (memoization), which will reduce the processing time after you start receiving queries (even if this means you have to do more preprocessing on the graph).

 ```
           1
         /   \
       2       3
             /   \
           5       4

  Fig 1.1
 ```

 Following are the observations we can make from the given:
  1. The graph is a Tree. We can arbitrarily select a "root", such that every other node has a "parent", a nonzero "depth", one or more "ancestors", etc.
  2. Once we've done that, the shortest path from node a to node b consists of node a, node b, all ancestors of a that aren't ancestors of b, all ancestors of b that aren't ancestors of a, and their "least common ancestor".
  3. From the tree in ***Fig1.1***, lets say we want to find the shortest path from node 2 to node 4.
      - Ancestors of 2: {1}
      - Ancestors of 4: {3,1}
      - Now was per algorithm in Pt.3; shortest path is Node 2 --> 1 --> 3 --> 4
  4. In a gist, we are basically trying to find the Lowest Common Ancestors (LCAs) for every parent of source and target (bottom up). This will eventually give us the shortest path between source and destination. For detailed explanation, refer to the link above.

Now what we do for Pre-processing:

 1. Represent the graph as a mapping from each node to a list of its neighbors. Ex:
      ```
      { 1:[2,3], 2:[1], 3:[1,5,4], 4:[3], 5:[3] }
      ```
 2. Choose a root node.
 3. Calculate and store each node's "parent" and "depth". (We can do this in O(N) time using depth-first search or breadth-first search.)
 4. For each pair of nodes, calculate and store their "least common ancestor". (We can do this in total time O(N2) using the results of the previous step and memoization using Dynamic Programming). Refer to link 2 for optimizing Pt 4. using Segments
 5. Initialize a mapping from each node to the number of times that it's the endpoint of a path, and a mapping from each node to the number of times that it's the least common ancestor of the endpoints of a path. (Note: if a given path is from a single node to itself, then we will count that as twice that it's the endpoint of a path — as well as once that it's the last common ancestor of the endpoints)

Now real time Post-Processing or Querying:

 1. Update the two mappings (described above in pt 5 from pre-processing)
 2. We can do this in O(1) time per query, for a total of O(Q) time.

Finally:
 - Do a post-order traversal of the graph, computing the number of paths that visited that node. The logic for this is as follows: the total number of paths that visited node a is equal to the sum of the numbers of paths that visited each of its children, minus the sum of the numbers of times that each of its children was the last common ancestor of a path's endpoint, plus the number of times that a itself was an endpoint, minus the number of times that a itself was the last common ancestor of a path's endpoint (to cancel out double-counting).
 - Return the node for which the previous step returned the greatest number. If multiple nodes are tied for greatest, then . . . I dunno, the problem statement was vague about this, you'll need to ask for requirements.

Overall, this requires O(N^2) preprocessing, O(Q) realtime processing per query, and O(N) postprocessing.
