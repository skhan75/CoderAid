"""
Given an array of integers and a window k, calculate the maximum sum of the consecutive sequence of nos
within the window size k

COMPLEXITY:
    - Runtime: O(log n)
    - Space Complexity: O(1)
"""


def k_maximum_sum(arr, k, n):
    max_sum = 0

    if n < k:
        return -1

    # Compute sum of first window of size k
    for i in range(k):
        max_sum += arr[i]

    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window.
    window_sum = max_sum

    for i in range(k, n):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(window_sum, max_sum)

    return max_sum


#Driver Code
input = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(input)

res = k_maximum_sum(input, k, n)

print (res)
