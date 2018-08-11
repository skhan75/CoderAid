
def first_substring(s, x):
    res = check(s,x)
    print (res)


def check(s, x):
    ls = len(s)
    lx = len(x)
    i,j,match = 0,0,0
    index = 0

    while i < ls and j < lx:
        if j > 0 and x[j] != s[i]:
            i -= 1
            j = 0

        if x[j] == s[i]:
            j += 1
            index = i


        i += 1

    return j == lx, index+1


s = "AGoogleIsBbIsAwesome"
x = "IsA"
first_substring(s, x)

s1 = "abcbcgl"
x1 = "bcgl"
first_substring(s1, x1)
