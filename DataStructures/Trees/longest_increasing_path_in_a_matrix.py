"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

neighbors = [[0,1], [1,0], [0,-1], [-1,0]]

"""
Approach 1 - Using Naive DFS
Time complexity : O(2m+n).
The search is repeated for each valid increasing path.
In the worst case we can have O(2m+n) calls

Space complexity : O(mn).
For each DFS we need O(h) space used by the system stack,
where hh is the maximum depth of the recursion.
In the worst case, O(h)=O(mn).
"""
def longestIncreasingPathNaive(mat):
    if len(mat) == 0:
        return 0

    r, c = len(mat), len(mat[0])

    ans = 0

    for i in range(r):
        for j in range(c):
            ans = max(ans, dfs(mat, i, j))

    return ans

def dfs(mat, i, j):
    ans = 0

    r, c = len(mat), len(mat[0])

    for nbr in neighbors:
        x, y = i + nbr[0], j + nbr[1]

        if x >= 0 and x < r and y >= 0 and y < c and mat[x][y] > mat[i][j]:
            ans = max(ans, dfs(mat, x, y))

    ans+=1

    return ans

"""
Approach 2 - Using DFS with Memoization
Time complexity : Time complexity : O(mn).
Each vertex/cell will be calculated once and only once,
and each edge will be visited once and only once.
The total time complexity is then O(V+E).
V is the total number of vertices and EE is the total number of edges.
In our problem, O(V)=O(mn), O(E)=O(4V)=O(mn).

Space complexity : O(mn).
"""
def longestIncreasingPathMemoized(mat):
    if len(mat) == 0:
        return 0

    r, c = len(mat), len(mat[0])
    cache = [[0 for i in range(c)] for j in range(r)]
    ans = 0

    for i in range(r):
        for j in range(c):
            ans = max(ans, dfs(mat, i, j, cache))

    return ans

def dfs(mat, i, j, cache):
    ans = 0

    r, c = len(mat), len(mat[0])

    # If current cell is already visited, then return ans from cache
    if cache[i][j] != 0:
        return cache[i][j]

    for nbr in neighbors:
        x, y = i + nbr[0], j + nbr[1]

        if x >= 0 and x < r and y >= 0 and y < c and mat[x][y] > mat[i][j]:
            cache[i][j] = max(cache[i][j], dfs(mat, x, y, cache))

    cache[i][j]+=1

    return cache[i][j]

def longestIncreasingPath(matrix):
    if not matrix: return 0
    m = len(matrix); n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]

    def helper(i,j):
        if not dp[i][j]:
            val = matrix[i][j]

            dp[i][j] = 1+max(helper(i+1,j) if i < m-1 and val > matrix[i+1][j] else 0,
                            helper(i-1,j) if i > 0 and val > matrix[i-1][j] else 0,
                            helper(i,j+1) if j < n-1 and val > matrix[i][j+1] else 0,
                            helper(i,j-1) if j > 0 and val > matrix[i][j-1] else 0)

        return dp[i][j]

    return max(helper(i,j) for i in range(m) for j in range(n))


if __name__ == "__main__":
    # nums = [[1,2]]
    nums = [[3,4,5],
            [3,2,6],
            [2,2,1]]

    # print longestIncreasingPathNaive(nums)
    print longestIncreasingPath(nums)
