import numpy as np
def longest_common_substring(s1, s2):
    rows = len(s1) + 1 # Add 1 to represent 0 valued row for DP
    cols = len(s2) + 1 # Add 1 to represent 0 valued col for DP

    T = [[0 for _ in range(cols)] for _ in range(rows)]

    print np.matrix(T)

    max_length = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if s1[i-1] == s2[j-1]:
                T[i][j] = T[i-1][j-1] + 1
                max_length = max(max_length, T[i][j])

    return max_length



if __name__ == '__main__':
    str1 = "abcdef"
    str2 = "zcdemf"
    expected = 3
    assert expected == longest_common_substring(str1, str2)
    str1 = "abcdef"
    str2 = "cde"
    expected = 3
    assert expected == longest_common_substring(str1, str2)
    str1 = "cde"
    str2 = "zcdemf"
    expected = 3
    assert expected == longest_common_substring(str1, str2)
