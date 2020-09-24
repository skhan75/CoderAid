class Solution(object):
    def combine(self, n, k):
        curr, output = [], []
        self.combine_util(n, k, 1, curr, output)
        return output

    def combine_util(self, n, k, first, curr, output):

        if len(curr) == k:
            print curr
            output.append(curr[:])
            print output

        for i in range(first, n+1):
            curr.append(i)

            self.combine_util(n, k, i+1, curr, output)

            curr.pop()





s = Solution()
print s.combine(4,2)
