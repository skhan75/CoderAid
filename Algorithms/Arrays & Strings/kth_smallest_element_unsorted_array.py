"""
Given an array on unsorted elements, find the kth smallest element.

LOGIC: We'll use partitioning logic from Quick Sort (Quick Select), where we select a pivot and partition
elements around it, but stop at the point where pivot itself is k’th smallest element.
Also, not to recur for both left and right sides of pivot,
but recur for one of them according to the position of pivot.

COMPLEXITY: The worst case time complexity of this method is O(n2), but it works in O(n) on average.
"""

def kth_smallest(arr, low, high, k):

    # If k is smaller than no of elements in the array
    if k > 0 and k < high - low + 1:

        piv = partition(arr, low, high)

        if piv-1 == k-1:
            return arr[piv]

        if piv-1 > k-1: # If pivot is greater than k, recur for the left subarray, cuz that's where the piv == k will be
            return kth_smallest(arr, low, piv-1, k)

        else: # Else recur for the right subarray
            return kth_smallest(arr, piv+1, high, k - piv+low-1)

    return None

def partition(arr, low, high):

    i = low # index of smaller element
    pivot = arr[high] # Picking the last element from right end as the pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[j] = arr[j], arr[i]

    return i




#Driver code
input = [2,5,8,1,4,22,21,11,56,13,43,7]
res = kth_smallest(input, 0, len(input)-1, 4) # 5

print (res)
