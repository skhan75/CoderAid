"""
Given an array of integers, determin if it could be divided into k equal sum partition.
COMPLEXITY:

"""

def has_k_equal_sum_parititons(arr, k, n):

    if k>n:
        return False

    total_sum = sum(arr)

    if total_sum%k != 0:
        print ('HERE')
        return False

    partition_table = [[True for i in range(n+1)] for j in range(total_sum//k + 1)]

    # Initialize left most column as False for all sum indexes but empty set
    for i in range(total_sum//k + 1):
        partition_table[i][0] = False

    # Initialize top most row as True for 0 sum for all elements in non empty set
    for i in range(n+1):
        partition_table[0][i] = True

    # Fill the partition table in bottom up manner
    row = n + 1
    col = total_sum//k + 1

    for i in range(1, col):
        for j in range(1, row):
            partition_table[i][j] = partition_table[i][j-1]

            if i >= arr[j-1]:
                partition_table[i][j] = partition_table[i][j] or partition_table[i - arr[j - 1]][j - 1]


    return partition_table[total_sum//k][n-1]



# Driver Code
arr = [4, 3, 2, 3, 5, 2, 1]
k = 4

print(has_k_equal_sum_parititons(arr, k, len(arr)))
