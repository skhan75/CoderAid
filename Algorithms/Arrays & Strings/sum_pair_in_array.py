"""
Given an unsorted array of integers, find the pair with the given sum in it.
Complexity: O(n) Using Hashsets
"""

def find_pair(arr, sum):

    # Create an empty Hash Set
    s = set()

    for e in arr:
        if (sum - e) in s:
            print ('Pairs are: ', e,',', sum-e)
        else:
            s.add(e)


if __name__ == "__main__":
    arr = [8,7,2,5,3,1]
    sum = 10
    res = find_pair(arr, sum)
