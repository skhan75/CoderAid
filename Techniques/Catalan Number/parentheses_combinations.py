
def parentheses_combinations_recursive(left, right, string, result):

    # When both left and right reaches 0, that means we have found a valid combination,
    # so we append it.
    if left == 0 and right == 0:
        result.append(string)

    # If we have left open bracket left, we add it
    if left > 0:
        parentheses_combinations_recursive(left-1, right+1, string+'(', result)

    # if we have a right bracket left we add it
    if right > 0:
        parentheses_combinations_recursive(left, right-1, string+')', result)

    return result

def parentheses_combinations_iterative(n):

    # If n is odd, we cannot create any valid parantheses
    if n & 1: # n%2
        return 0

    # Otherwise return n/2'th
    # Catalan Numer
    return catalan(n//2)

# A Binomial coefficient based
# function to find nth catalan
# number in O(n) time
def catalan(n):
    c = binomial_coefficient(2*n, n)

    # return 2nCn/(n+1)
    return int(c / (n + 1));

# Returns value of Binomial
# Coefficient C(n, k)
def binomial_coefficient(n, k):
    res = 1

    # Since C(n, k) = C(n, n-k)
    if (k > n - k):
        k = n - k

    # Calculate value of [n*(n-1)*---
    # *(n-k+1)] / [k*(k-1)*---*1]
    for i in range(k):
        res *= (n - i)
        res /= (i + 1)

    return int(res)


# Driver Code
n = 4
print (parentheses_combinations_iterative(n*2))
print (parentheses_combinations_recursive(n,0,'',[]))
