"""
Find the edit distance between two given strings.
Edit distance is the minimum number of operations required to
modify one string into the second one or vice versa.
The operations allowed are as follows:

1. Delete a character

2. Replace a character with another one

3. Insert a character

Brute Force Approach using Recursion: (For optimized solution,
refer to minimum_edi_distance.py in Dynamic Programming)
--------------------------------------------------------------


"""

def edit_distance(s1, s2, m, n):
    if len(s1) == m:
        return len(s1) - n

    if len(s2) == n:
        return len(s1) - m

    if s1[m] == s2[n]:
        return edit_distance(s1, s2, m+1, n+1)

    if s1[m] != s2[n]:
        return 1 + min( min (
            edit_distance(s1,s2,m,n+1),
            edit_distance(s1,s2,m+1,n),
            edit_distance(s1,s2,m+1,n+1)
        ))


def minimum_edit_distance(s1, s2):
    return edit_distance(s1, s2, 0, 0)


if __name__ == '__main__':
    str1 = "azced"
    str2 = "abcdef"
    expected = 3
    print (minimum_edit_distance(str1, str2))
    # assert expected == min_edit_distance(str1, str2)
    # assert expected == min_edit_distance(str2, str1)
