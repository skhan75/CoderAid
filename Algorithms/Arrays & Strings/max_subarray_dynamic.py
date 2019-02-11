"""
Maximum SubArray sum also handles when all the nos are negative

Complexity: O(n)
"""
def max_subarray_sum(arr):

    max_so_far = arr[0]
    current_max = arr[0]

    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max+arr[i])
        max_so_far = max(max_so_far, current_max)

    return max_so_far

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print ("Maximum contiguous sum is" , max_subarray_sum(a))
