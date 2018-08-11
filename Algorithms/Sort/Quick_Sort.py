def partition(array, low, high):
    # index of left most element
    i = (low-1)
    # pivot element
    pivot = array[high]

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]

    return (i+1)

def quick_sort(array, low, high):
    if low < high:

        # pi is the rightmost element
        pi = partition(array, low, high)

        # separating elements before and after the pivot
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)



array = [10,2,90,80,70,30,40,25,44,99,100,23,1,4,5,6,8,9,11,101]
n = len(array)-1
quick_sort(array, 0, n)
print (array)
