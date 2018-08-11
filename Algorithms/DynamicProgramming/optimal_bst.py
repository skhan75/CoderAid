def min_cost_bst(array, freq):

    size = rows = cols = len(array)

    T = [[0 for _ in range(size)] for _ in range(size)]

    # Now fill all the diagonal with its frequencies when root = 1
    for i in range(rows):
        T[i][i] = freq[i]

    # l --> sub tree size
    for l in range(2, size+1):
        for start in range(size + 1 - l):
            end = start + l - 1
            T[start][end] = float('inf')
            total = sum(freq[start:end + 1])

            for k in range(start, end+1):
                val = total + (0 if k - 1 < 0 else T[start][k - 1]) + (0 if k + 1 > end else T[k + 1][end])
                T[start][end] = min(val, T[start][end])

    return T[0][-1]


if __name__ == '__main__':
    input_array = [10, 12, 16, 21]
    freq = [4, 2, 6, 3]
    expected = 26
    assert expected == min_cost_bst(input_array, freq)
    # input_array = [10, 12, 20, 35, 46]
    # freq = [34, 8, 50, 21, 16]
    # expected = 232
    # assert expected == min_cost_bst(input_array, freq)
