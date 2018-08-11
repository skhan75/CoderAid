# Finding an element from the sorted matrix
# Sorted --> sorted by row and sorted by column
def find(mat, row, col, x):
    element = mat[row][col]

    if x != element and (row >= len(mat) - 1 or col <= 0):
        return False

    if x == element:
        return (row, col)
    elif x > element:
        return find(mat, row+1, col, x)
    else:
        return find(mat, row, col-1, x)


if __name__ == "__main__":
    mat = [[10, 20, 30, 40, 50],
           [15, 25, 35, 45, 55],
           [27, 29, 37, 48, 59],
           [32, 33, 39, 50, 62],
           [38, 41, 44, 58, 66]]

    x = 62
    i = 0
    j = len(mat[0])-1

    res = find(mat, i, j, x)

    if res:
        print('Element found at position ', res)
    else:
        print('Element not found..')
