"""
Problem Statement
=================
Given an array of non negative numbers and a total, is there subset of numbers in this array which adds up to given
total. Another variation is given an array is it possible to split it up into 2 equal sum partitions. Partition need not
be equal sized. Just equal sum.
Video
-----
* https://youtu.be/s6FhG--P7z0
Solution
--------
* Time complexity is O(input.size * total_sum)
* Space complexity is O(input.size*total_sum)

"""


def subset_sum(sequence, sum_value):
    import numpy as np
    cols = sum_value + 1
    rows = len(sequence) + 1

    T = [[False for _ in range(cols)] for _ in range(rows)]

    # If sum_value is 0, then all sequence elements are True
    for row in range(rows):
        T[row][0] = True

    for i in range(1,rows):
        for j in range(1, cols):
            if j >= sequence[i-1]:
                T[i][j] = T[i-1][j] or T[i-1][j - sequence[i-1]]
            else:
                T[i][j] = T[i-1][j]

    return T[rows-1][cols-1]


def partition(sequence):
    sequence_sum = sum(sequence)

    if sequence_sum % 2 != 0:
        return False

    expected = sequence_sum / 2

    return subset_sum(sequence, expected)


if __name__ == '__main__':
    sequence = [2, 3, 7, 8]
    assert True == subset_sum(sequence, 11)

    sequence = [1, 3, 5, 5, 2, 1, 1, 6]
    assert True == partition(sequence)
