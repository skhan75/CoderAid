# https://www.youtube.com/watch?v=e5ik2UGjHBk

def sort(arr):
    return merge_sort(arr, [0]*(len(arr)), 0, len(arr)-1)

def merge_sort(arr, aux, left_start, right_end):
    if left_start < right_end:
        # get the middle
        mid = (left_start + right_end) // 2
        print 'mid', mid
        # split halves into left and right indexes
        merge_sort(arr, aux, left_start, mid)
        merge_sort(arr, aux, mid+1, right_end)
        # sort and merge halves
        merge(arr, aux, left_start, right_end)

def merge(arr, aux, left_start, right_end):
    # first index for the left split
    print 'left start --> ', left_start, 'right_end', right_end
    left_end = (left_start + right_end)  // 2
    print 'left end --> ', left_end
    # first index for the right split
    right_first = left_end + 1
    print 'right first', right_first
    # total no of elements that we're gonna copy
    size = right_end - left_start + 1
    # Initial index of first/left subarray
    left = left_start
    # Initial index of second/right subarray
    right = right_first
    # Initial index of merged subarray
    index = left_start

    while left <= left_end and right <= right_end:
        if arr[left] <= arr[right]:
            aux[index] = arr[left]
            left += 1
        else:
            aux[index] = arr[right]
            right += 1
        index += 1

    # Copy the remaining elements of left, if any
    while left <= left_end:
        aux[index] = arr[left]
        left += 1
        index += 1

    # Copy the remaining elements of right, if any
    while right <= right_end:
        aux[index] = arr[right]
        right += 1
        index += 1

    # Copying from auxillary array to original
    arr[:index] = aux[:index]


if __name__ == "__main__":
    arr = [5,6,7,4,5,21,1,43,9]
    sort(arr)
    print(arr)
