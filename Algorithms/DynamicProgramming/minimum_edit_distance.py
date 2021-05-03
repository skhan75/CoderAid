"""
    Converting one string to snother string in minimum conversions possible
"""

def min_edit_distance(s1, s2):
    rows = len(s1) + 1 # 1 for extra indices
    cols = len(s2) + 1

    T = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        T[i][0] = i

    for j in range(cols):
        T[0][j] = j

    for i in range(1,rows):
        for j in range(1,cols):
            if s1[i-1] == s2[j-1]:
                T[i][j] = T[i-1][j-1]
            else:
                T[i][j] = 1 + min(T[i-1][j-1], T[i][j-1], T[i-1][j])

    print_edits(T, s1, s2)
    return T[rows - 1][cols - 1]


def print_edits(T, s1, s2):
    rows = len(T) - 1
    cols = len(T[0]) - 1

    while True:
        if rows == 0 and cols == 0:
            break

        if s1[rows-1] == s2[cols-1]:
            rows -= 1
            cols -= 1

        elif T[rows][cols] == T[rows - 1][cols - 1] + 1:
            print "Edit %s in string1 to %s in string2." % (s2[cols - 1], s1[rows - 1])
            rows -= 1
            cols -= 1
        elif T[rows][cols] == T[rows - 1][cols] + 1:
            print "Delete %s in string2." % s1[rows- 1]
            rows -= 1
        elif T[rows][cols] == T[rows][cols - 1] + 1:
            print "Delete %s in string1." % str1[cols - 1]
            cols -= 1

if __name__ == '__main__':
    str1 = "azced"
    str2 = "abcdef"
    expected = 3
    assert expected == min_edit_distance(str1, str2)
    assert expected == min_edit_distance(str2, str1)
