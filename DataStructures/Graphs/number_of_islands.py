
class Graph:

    def __init__(self, r, c, g):
        self.row = r
        self.col = c
        self.graph = g

    # Function to check if a given cell (row, col) can be included in DFS
    def is_safe(self, i, j, visited):
           # row number is in range, column number
        # is in range and value is 1
        # and not yet visited
        return (i >= 0 and i < self.row and
                j >= 0 and j < self.col and
                not visited[i][j] and self.graph[i][j])

    def dfs(self, row, col, visited):
        # Following are th 8 possible movements (neighbors) around a given cell
        row_neighbors = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_neighbors = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Mark the current cell as visited
        visited[row][col] = True

        # Recur all connected 8 neighbors
        for i in range(8):
            current_nbr_row_idx = row + row_neighbors[i]
            current_nbr_col_idx = col + col_neighbors[i]
            if self.is_safe(current_nbr_row_idx, current_nbr_col_idx, visited):
                self.dfs(current_nbr_row_idx, current_nbr_col_idx, visited)

    def count_islands(self):
        visited = [[False for i in range(self.col)] for j in range(self.row)]

        if self.graph is None:
            return 0

        count = 0
        for i in range(self.row):
            for j in range(self.col):
                # If a cell value is 1 and is not yet visited, its our new found island
                if visited[i][j] == False and self.graph[i][j] == 1:
                    self.dfs(i, j, visited)
                    count += 1


        return count



if __name__ == "__main__":
    graph = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]

    row = len(graph)
    col = len(graph[0])

    g = Graph(row, col, graph)

    print "Number of islands is:"
    print g.count_islands()
