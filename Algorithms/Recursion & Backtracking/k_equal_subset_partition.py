"""
Given an array of integers, determin if it could be divided into k equal sum partition.
REFERENCE: https://github.com/bephrem1/backtobackswe/blob/master/Dynamic%20Programming%2C%20Recursion%2C%20%26%20Backtracking/partitionIntoKEqualSumSubsets.java
COMPLEXITY:
    - Runtime: O(Highly Exponential) ~ O(2^n)
    - Space: O(n)
"""

def has_k_equal_sum_parititons(arr, k, n):

    total_sum = sum(arr)

    if n < k:
        return False

    if k == 0 or total_sum%k != 0:
        return False

    target_sum_per_bucket = total_sum // k

    used = [False for i in range(n)]
    return parition_util(0, arr, used, k, 0, target_sum_per_bucket)


def parition_util(start, arr, used, k, current_bucket_sum, target_sum_per_bucket):
    # If one bucket is left, we're already sure that its gonna have the rest of the
    # elements with equal sum
    if k == 1:
        return True

    # If current bucket sum has reached target sum,
    # We recurse back with 1 bucket less (k-1)
    if current_bucket_sum == target_sum_per_bucket:
        return parition_util(0, arr, used, k-1, 0, target_sum_per_bucket)

    # Now we Explore other possibilities
    for i in range(start, len(arr)):
        if used[i] is False:
            used[i] = True # Choose

            # Explore
            if parition_util(i+1, arr, used, k, current_bucket_sum + arr[i], target_sum_per_bucket):
                return True

            used[i] = False # Unchoose

    return False



# Driver Code
arr = [4, 3, 2, 3, 5, 2, 1]
k = 4

print(has_k_equal_sum_parititons(arr, k, len(arr)))
