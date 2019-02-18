## Most Visited Node in a Graph

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
 Here in our case, it seems like we have redundancy in terms of time and processing, but we can have ample of space to store the pre-processed meta information (memoization), which will reduce the processing time after you start receiving queries.
