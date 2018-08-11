def longest_palindromic_subsequence(string):
    size = rows = cols = len(string)

    T = [[0 for _ in range(cols)] for _ in range(rows)]

    # Fill all the diagonal elements with 1s,
    # since each character is a palindrom of itself
    for i in range(rows):
        T[i][i] = 1

    # l --> substring length
    for l in range(2, size + 1):
        print 'l-->', l
        for row in range(size + 1 - l):
            col = row + l - 1
            print 'row', row, ' col', col
            if string[row] == string[col]:
                if size == 2:
                    T[row][col] = 2
                else:
                    T[row][col] = 2 + T[row+1][col-1]

            else:
                T[row][col] = max(T[row][col-1], T[row+1][col])


    return T[0][-1]


if __name__ == '__main__':
    given_string = "agbdba"
    expected_result = 5
    assert expected_result == longest_palindromic_subsequence(given_string)
