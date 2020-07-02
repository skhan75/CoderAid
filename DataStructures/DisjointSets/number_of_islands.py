class UnionFind:

    def __init__(self, rank=0, parent=None):
        self.rank = rank
        self.parent = parent
        self.count = 0




def count_islands(grid):
    if grid == None or len(grid) == 0:
        return 0

    row_len = len(grid)
    col_len = len(grid[0])



if __name__ == "__main__":
    grid =  [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]


    print "Number of Islands ", count_islands(grid)
