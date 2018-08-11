import numpy as np

def longest_common_subsequence(s1, s2):
    cols = len(s1) + 1   # Add 1 to represent 0 valued column for DP
    rows = len(s2) + 1   # Add 1 to represent 0 valued column for DP

    T = [[0 for _ in range(cols)] for _ in range(rows)]

    max_length = 0
    answer = []

    for i in range(1, rows):
        for j in range(1, cols):
            # If characters match
            if s2[i-1] == s1[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
                answer.append(s2[i-1])
            else:
                T[i][j] = max(T[i][j-1], T[i-1][j])

            max_length = max(max_length, T[i][j])

    print answer

    return max_length



if __name__ == '__main__':
    sequence1 = "ABCDGHLQR"
    sequence2 = "AEDPHR"
    expected_length = 4
    assert expected_length == longest_common_subsequence(sequence1, sequence2)
    assert expected_length == longest_common_subsequence(sequence2, sequence1)
