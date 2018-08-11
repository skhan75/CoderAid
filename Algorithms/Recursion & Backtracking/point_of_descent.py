#
# Author: Sami Ahmad Khan
# File_overview: Finding Point Of Descent
# **
#   You are given an array that is comprised of positive integers.
#   Initially, these numbers are ascending, but at some point they start descending.
#   There are no duplicate integers in the array.
# **
#

# Binary Search Approach -- Complexity: O(log N)
def find(list, left, right):
    if right > left:
        mid = left + (right-1) // 2

        if list[mid] > list[mid-1] and list[mid] > list[mid+1]:
            return list[mid]

        elif list[mid] < list[mid-1]:
            return find(list, left, mid)

        elif list[mid] < list[mid+1]:
            return find(list, mid, right)
    else:
        return -1

def point_of_descent(list):
    return find(list, 0, len(list))

if __name__ == "__main__":
    print (point_of_descent([1,2,3,4,5,16,15,14,13,12,11,10,9,8,7,6]))
