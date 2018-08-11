#Find if the shorter string is a subsequence of the longer string
# Output the second index corresponding to the first one, requiring output only
# If there is only one match, and false if there is more than one pair
# a b c d e f g, a b -> [0,1]
# a b b c, ab c -> False

def is_subsequence(s1, s2):
    if len(s1) > len(s2):
        main_string, sub_string = s1, s2
    else:
        main_string, sub_string = s2, s1

    res = check(main_string, sub_string)

    if res[0] == True:
        return res[1]
    else:
        return res[0]

def check(main_string, sub_string):
    m = len(main_string)
    n = len(sub_string)

    i,j,matches = 0,0,0
    indexes = []

    while i < m:
        if sub_string[j] == main_string[i]:
            indexes.append(j)
            j+=1
        if n == j:
            matches += 1
            j = 0
        i+=1

    return matches == 1, indexes


if __name__ == "__main__":
    s1 = "abcdefghesa"
    s2 = "ab"
    print (is_subsequence(s1, s2))

    s3 = "abcdefghabc"
    s4 = "abc"
    print (is_subsequence(s3,s4))
