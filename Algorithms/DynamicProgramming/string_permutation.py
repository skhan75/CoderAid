#Complexity --> n! for each permuation. So it is O(nxn!)
def permutate(s, left, right, exists):
    if left == right:
        s = ''.join(s)
        if s not in exists:
            exists.append(s)
            return

    else:
        for i in range(left, right+1):
            s[left], s[i] = s[i], s[left]   # Replace characters

            permutate(s, left+1, right, exists)     # Keep iterating each element marking them as left
                                            # This is to keep some index of the string to stay constant
            s[left], s[i] = s[i], s[left]   # backtrace

    return exists


if __name__ == "__main__":
    s = input().strip()
    s = list(s)
    print (permutate(s, 0, len(s)-1, []))

# Recursion Tree
#                                        ABC
#               |A|BC                   |B|AC               |C|BA
#          |AB|C     |AC|B          |BA|C   |BC|A       ... so on..
#
