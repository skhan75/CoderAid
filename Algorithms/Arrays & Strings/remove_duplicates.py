
def remove_duplicates(arr, n):

    j = 0
    arr.sort()

    for i in range(0, n-1):

        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1

    arr[j] = arr[n-1]

    # Slice all the elements after j
    arr = arr[:j+1]

    return arr


# Driver Method
arr = [5,2,3,4,5,9,8,5,1,10,8,10]

print remove_duplicates(arr, len(arr))
