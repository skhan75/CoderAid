"""
Maximum Subarray Sum using Divide and Conquer algorithm

You are given a one dimensional array that may contain both
positive and negative integers, find the sum of contiguous subarray of
numbers which has the largest sum.
For example, if the given array is {-2, -5, 6, -2, -3, 1, 5, -6},
then the maximum subarray sum is 7 (see highlighted elements).

Algorithm:
    - Divide the array into two equal sub arrays
    - Recursively calculate the maximum sub array sum for the left subarray
    - Recursively calculate the maximum sub array sum for the right subarray
    - Find the maximum sub array sum that crosses the mid element
    - Return the max of the above three sums

Complexity: O(nlogn)
"""

def max_crossing_sum(arr, left, mid, right):
    # Include elements on left of mid.
    sum = 0
    left_sum = float("-inf")

    # Iterate in reverse from mid --> left - 1 for left sum
    for i in range(mid, left-1, -1):
        sum  += arr[i]

        if (sum > left_sum) :
            left_sum = sum

    # Include elements on right of mid.
    sum = 0
    right_sum = float("-inf")

    # Iterate from mid --> right + 1 for right sum
    for i in range(mid+1, right+1):
        sum  += arr[i]

        if (sum > right_sum) :
            right_sum = sum

     # Return sum of elements on left and right of mid
    return left_sum + right_sum


def max_subarray_sum(arr, left, right):
    # Base Case - If array contains only one element, return that element
    # Meaning return from the sub problem, when its broken down till 1 element is left
    if left == right:
        return arr[left]

    # Find the middle point
    mid = ( left + right ) // 2

    # Return maximum of following three possible cases
    # a) Maximum subarray sum in left half
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the
    #     subarray crosses the midpoint
    return max(max_subarray_sum(arr, left, mid),
               max_subarray_sum(arr, mid+1, right),
               max_crossing_sum(arr, left, mid, right))

arr = [2, 3, -4, 5, -7]
n = len(arr)

max_sum = max_subarray_sum(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)
