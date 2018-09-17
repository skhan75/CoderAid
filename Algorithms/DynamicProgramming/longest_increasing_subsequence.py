"""
LONGEST INCREASING SUBSEQUENCE:

APPROACH 1: Complexity --> O(n^2)

"""

# 3, 4, -1, 0, 6, 2, 3
def longest_increasing_subsequence_n2(input):
    print ('INPUT', input)
    T = [1 for _ in range(len(input))]
    solution_indices = [ _ for _ in range(len(input))]

    # Let i start from the first position
    for i in range(1, len(input)):
        # And j from 0 till i
        for j in range(0, i):
            if input[j] < input[i] and T[i] < T[j] + 1:
                T[i] = T[j] + 1
                solution_indices[i] = j

    max_value = max(T)
    max_index = T.index(max_value)

    # Print solution using linked values in solution_indices
    # next_index = max_index
    #
    # while True:
    #     print (input[next_index]),
    #
    #     old_index = next_index
    #     next_index = solution_indices[next_index]
    #     print ('nxt inx', next_index)
    #     if next_index == old_index:
    #         break

    tmp = max_value
    indexes = []
    print (T)
    for i in range(len(input)):
        print (tmp)
        if T[i] == tmp:
            print (T[i])
            indexes.append(i)
            tmp = tmp - 1
            print ('here', tmp)

    print (indexes)

    return T[max_index]



# """
# LONGEST INCREASING SUBSEQUENCE:
#
# APPROACH 2: Complexity --> O(nlogn)
# Strategy:
# 	Case 1:
# 		If A[i] is the smallest among all end candidates of the Active list,
# 		then we'll start a new active list of length 1.
#
# 	Case 2:
# 		If A[i] is largest among all the end candidates of Activen list,
# 		then we'll clone the largest active list and extend it by A[i]
#
# 	Case 3:
# 		If A[i] is in between, we'll find a list with the largest end element that is
# 		smaller than A[i]. Clone and extend this list by A[i]. We'll discard all other lists
# 		of same length as that of this modified list.
# """
#
# # Binary Search
# # A[] is ceil index in the caller
# def get_ceil_index(input, l, r, T, key):
# 	#This is a Ubiquitous Binary Search Algorithm with fewer no of comparisons.
#     while r - l > 1:
#         mid = l + (r-1) // 2
#         if input[T[mid]] >= key: # Gives the Ceil
# 			r = mid
#         else:
# 			l = mid
#         return r
#
# def longest_increasing_subsequence_nlogn(input):
#     # stores the indices of temporary intermediate results
#     T = [None] * len(input)
#     # Final Resultant indices
#     R = [-1] * len(input)
#
#     # Put the index of the first element
#     T[0] = 0
#     count = 0
#
#     for i in range(1,len(input)):
#         # if input i is less than 0th value of element at T[0], then REPLACE it right there
#         if input[T[0]] > input[i]:
#             T[0] = i
#
#         # if input i is greater than last value of T, then APPEND its index
#         elif input[T[count]] < input[i]:
#             count += 1
#             T[count] = i
#             R[T[count]] = T[count-1]
#
#         #else do a binary search to find the ceil of input[i] and REPLACE it
#         else:
#             index = get_ceil_index(input, 0, count, T, input[i])
#             # We replace the index of the ceiling with the current index
#             T[index] = i
#             # And add in R where this new index is coming from
#             R[T[index]] = T[index-1]
#
#     # Printing increasing subsequence in reverse order
#     index = T[count]
#     while index != -1:
#         print (input[index])
#         index = R[index]
#
#     return count
#
#
if __name__ == "__main__":
    input = [ 3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10 ]

    result_n2 = longest_increasing_subsequence_n2(input)
    print ("Result: ", result_n2)

    # result_nlogn = longest_increasing_subsequence_nlogn(input)
    # print "Result: ", result_nlogn
