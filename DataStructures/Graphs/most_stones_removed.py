"""
Approach 1: Depth-First Search
Intuition

Let's say two stones are connected by an edge if they share a row or column,
define a connected component in the usual way for graphs:
a subset of stones so that there doesn't exist an edge from a stone
in the subset to a stone not in the subset. For convenience,
we refer to a component as meaning a connected component.

The main insight is that we can always make moves that reduce the number of stones in
each component to 1.

Firstly, every stone belongs to exactly one component, and moves in one component
do not affect another component.

Now, consider a spanning tree of our component. We can make moves repeatedly
from the leaves of this tree until there is one stone left.

Algorithm

To count connected components of the above graph, we will use depth-first search.

For every stone not yet visited, we will visit it and any stone in the same
connected component. Our depth-first search traverses each node in the component.

For each component, the answer changes by -1 + component.size.
"""
import collections
class Solution(object):
    def removeStones(self, stones):
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            print 'i', i, 'x',x
            for j in xrange(i):
                print 'j', j
                y = stones[j]
                print 'y', y
                # Shares row and col
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)
                    print graph

            print '\n'

        print graph

        N = len(stones)
        ans = 0

        seen = [False] * N
        for i in xrange(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                ans -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print s.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
