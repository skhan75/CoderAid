import numpy as np

# Function to calculate sum between two indices
def sum(A, fro, to):
    total = 0
    for i in range(fro, to+1):
        total += A[i]
    return total

def partition_recursive(A, n, k):
    # If there is just one partition, then we return sum of all the
    # nos, since he has to cover all the elements
    if k == 1:
        return sum(A, 0, n-1)

    # If there is just one board
    if n == 1:
        return A[0]

    # Assign a max best
    best = float('inf')

    # Putting k-1th divider between A[i-1] and A[j]
    # we try to find the minimum of all the maximum partitions to the
    # left of A[i]
    for i in range(1,n):
        best = min(best, max(partition_recursive(A, i, k-1), sum(A, i, n-1)))

    return best


""" The above recursive method has an overlapping subproperty, and some of the
problems are being solved again and again. To reduce this, we memoize using top down"""
def partition_dp(A, n, k):

    # Initialize table
    T = [[0 for _ in range(n+1)] for _ in range(k+1)]

    # Initialize base cases

    # 1. When k = 1, write the summation for elements 0 --> i-1
    for i in range(n+1):
        T[1][i] = sum(A, 0, i-1)

    # 2. When n = 1, put A[0] for the whole 1st column
    for i in range(k+1):
        T[i][1] = A[0]

    # 2 to k partitions
    for i in range(2, k+1):
        # 2 to n boards
        for j in range(2, n+1):

            # Track minimum
            best = float('inf')

            # Pivot or i-1th separator before position A[p=1...j]
            for p in range(1, j+1):
                best = min(best, max(T[i-1][p], sum(A, p, j-1)))

            T[i][j] = best

    return T[k][n]

"""
    Above DP approach gives a Runtime complexity of O(nk^2) and Space complexity
    of O(nk). This can further be reduced by using a more efficient approach of
    Binary Search. The invariant of Binary Search has two main parts:
        * The target value would always be in the searching range
        * The searching range will be decreased in each loop so termination can be reached
    Time Complexity of this approach is --> O(N log(sum(arr[])))
"""

'''
find minimum required painters for given maxlen
which is the maximum length a painter can paint
'''
def get_no_of_painters(A, n, max_len):
    total = 0
    num_painters = 1

    for i in range(0, n):
        total += A[i]
        if total > max_len:
            total = A[i]
            num_painters += 1

    return num_painters

# Returns the max element in range n
def get_max_element(A, n):
    max = float('-inf')
    for i in range(n):
        if A[i] > max:
            max = A[i]

    return max

# Returns the sum between A to n
def get_max_sum(A, n):
    total = 0
    for i in range(n):
        total += A[i]

    return total


def partition_optimized(A, n, k):
    '''
    The idea of getting low and high here as Max element and Max sum is providing the
    range of search, which can be as low as value of one element in the sequence to the
    maximum sum in the sequence.
    '''
    low = get_max_element(A, n)
    high = get_max_sum(A, n)

    '''
    We are going to find that mid element (maximum sum) which will encompass
    all k partitions such that the mid represents the minimum of maximum of
    sum of partitions
    '''

    while low < high:

        mid = low + (high-low) // 2
        required_painters = get_no_of_painters(A, n, mid)

        # Find better optimum in lower half of the searching criteria.
        # Here mid is included because we may not get anything better
        if required_painters <=  k:
            high = mid

        # Find better optimum in upper half of the searching criteria.
        # Here mid is excluded because it gives required_painters > k,
        # which is invalid
        else:
            low = mid + 1

    return low



if __name__ == "__main__":

    arr = [10, 20, 60, 50, 30, 40]
    k = 3
    expected = 90
    assert expected == partition_recursive(arr, len(arr), k)
    k = 2
    expected = 120
    assert expected == partition_recursive(arr, len(arr), k)
    k = 3
    expected = 90
    assert expected == partition_dp(arr, len(arr), k)
    k = 3
    expected = 90
    assert expected == partition_optimized(arr, len(arr), k)
