#
# A string consists of ‘0’, ‘1’ and '?'. The question mark can be either '0' or '1'.
# Find all possible combinations for a string.
# Courtesy: GeeksForGeeks - https://www.geeksforgeeks.org/generate-all-binary-strings-from-given-pattern/
#

def print_permutations(S,i):
    if len(S) == i:
        print S
        return

    if S[i] == '?':
        # replace '?' by '0' and recurse
        S[i] = '0'
        print_permutations(S, i+1)

        # replace '?' by '1' and recurse
        S[i] = '1'
        print_permutations(S, i+1)

        # NOTE: Need to backtrack as string
        # is passed by reference to the
        # function
        S[i] = '?'
        # Note that you must set a position back to '?' after exploring that branch,
        # because you may be coming from another branch,
        # and later you will need to recognize this same position
        # as having a question mark again.

    else:
        print_permutations(S, i+1)

def permutations(S):
    return print_permutations(S, 0)

if __name__ == "__main__":
    s = "1??0?101"
    str = list(s)
    permutations(str)
