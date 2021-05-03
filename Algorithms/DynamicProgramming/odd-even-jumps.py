"""
You are given an integer array A.  From some starting index, you can make a series of jumps.  The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.

You may from index i jump forward to index j (with i < j) in the following way:

During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
(It may be the case that for some index i, there are no legal jumps.)
A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)

Return the number of good starting indexes.

Courtesy: LeetCode

EXPLANATION:

We need to jump higher and lower alternately to the end.

Take [5,1,3,4,2] as example.

If we start at 2,
we can jump either higher first or lower first to the end,
because we are already at the end.
higher(2) = true
lower(2) = true

If we start at 4,
we can't jump higher, higher(4) = false
we can jump lower to 2, lower(4) = higher(2) = true

If we start at 3,
we can jump higher to 4, higher(3) = lower(4) = true
we can jump lower to 2, lower(3) = higher(2) = true

If we start at 1,
we can jump higher to 2, higher(1) = lower(2) = true
we can't jump lower, lower(1) = false

If we start at 5,
we can't jump higher, higher(5) = false
we can jump lower to 4, lower(5) = higher(4) = false


COMPLEXITY:

Time O(NlogN)
Space O(N)

[5,1,3,4,2]

"""

def oddEvenJumps(A):
    N = len(A)

    def make(B):
        ans = [None] * N
        stack = []  # invariant: stack is decreasing
        for i in B:
            while stack and i > stack[-1]:
                ans[stack.pop()] = i
            stack.append(i)
        return ans

    B = sorted(range(N), key = lambda i: A[i])
    print B
    oddnext = make(B)
    print oddnext
    B.sort(key = lambda i: -A[i])
    print B
    evennext = make(B)
    print evennext

    odd = [False] * N
    even = [False] * N
    odd[N-1] = even[N-1] = True

    for i in xrange(N-2, -1, -1):
        if oddnext[i] is not None:
            odd[i] = even[oddnext[i]]
        if evennext[i] is not None:
            even[i] = odd[evennext[i]]
    print odd
    return sum(odd)

# def oddEvenJumps(A):
#         n = len(A)
#         next_higher, next_lower = [0] * n, [0] * n
#
#         stack = []
#         for i, a in enumerate(A):
#             print i
#         # for a, i in sorted([a, i] for i, a in enumerate(A)):
#         #     print a, i
#             # while stack and stack[-1] < i:
#             #     next_higher[stack.pop()] = i
#             # stack.append(i)
#
#         # stack = []
#         # for a, i in sorted([-a, i] for i, a in enumerate(A)):
#         #     while stack and stack[-1] < i:
#         #         next_lower[stack.pop()] = i
#         #     stack.append(i)
#         #
#         # higher, lower = [0] * n, [0] * n
#         # higher[-1] = lower[-1] = 1
#         # for i in range(n - 1)[::-1]:
#         #     higher[i] = lower[next_higher[i]]
#         #     lower[i] = higher[next_lower[i]]
#         # return sum(higher0)


if __name__ == "__main__":
    print oddEvenJumps([10,13,12,14,15])
