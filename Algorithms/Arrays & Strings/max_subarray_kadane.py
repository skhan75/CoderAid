# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
# from sys import maxint
#
# Simple idea of the Kadane’s algorithm is to look
# for all positive contiguous segments of the array
# (max_ending_here is used for this).
# And keep track of maximum sum contiguous segment among all
# positive segments (max_so_far is used for this). Each time we get a
# positive sum compare it with max_so_far and update max_so_far if it is greater than max_so_far
#
# 
def maxSubArraySum(a,size):

    max_so_far = float("-inf")
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

# Driver function to check the above function
a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print ("Maximum contiguous sum is", maxSubArraySum(a,len(a)) )
