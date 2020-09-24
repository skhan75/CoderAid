"""
LOGIC:
------

We basically keep a count of ith bits set ( assuming 32 bits or 8 bits whatever ),
by shifting bit to the left (which is actually 2^i)
i.e. which ith bit from (1 << i) bits gives a value with arr[j].
If yes, then we keep a count of the set and then use the following formula for the answer:
    ans += <Count of Set that had value from AND operation> * <Remaining elements that didn't form the set> * 2 (2 for the pair combination)
    i.e. ans += count * (n-count) * 2

COMPLEXITY:
-----------
O(n x 32) if 32 bits are considered
"""
def sumBitDifferences(arr,n):

    ans = 0  # Initialize result

    # traverse over all bits
    for i in range(0, 32):
        # count number of elements with i'th bit set
        count = 0
        for j in range(0,n):
            # Check the AND operation between element and shift
            if ( (arr[j] & (1 << i)) ):
                count+=1

        # Add "count * (n - count) * 2" to the answer
        ans += (count * (n - count) * 2);

    return ans

# Driver prorgram
arr = [1, 3, 6]
n = len(arr )
print(sumBitDifferences(arr, n))
