def maximum_sub_square_matrix(array):

    result = [ [ 0 for _ in range(len(array)) ] for _ in range(len(array)) ]
    max = 0

    for i in range(len(array)):
        result[i][0] = array[i][0]
        if result[i][0] == 1:
            max = 1

    for i in range(len(array)):
        result[0][i] = array[0][i]
        if result[0][i] == 1:
            max = 1

    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == 0:
                continue

            # if it is 1, then we get minimum of top, diagonal and left
            t = min(result[i-1][j], result[i-1][j-1], result[i][j-1])
            result[i][j] = t+1

            if result[i][j] > max:
                max = result[i][j]

    return max


if __name__ == "__main__":
    array = [
                [0,1,1,0,1],
                [1,1,1,0,0],
                [1,1,1,1,0],
                [1,1,1,0,1]
            ]
    expected = 3
    assert expected == maximum_sub_square_matrix(array)
