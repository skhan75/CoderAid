class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_steps = 0

        if n < 1:
            return 0

        # Using just 1, we can do n steps, so that is 1 step
        total_steps = 1

        while n//2 != 1:

            n = n//2
            print (n)
            no_of_twos = 2*n
            no_of_ones = n - no_of_twos
            total_steps += 1
            print ("STEPS", total_steps)

        return total_steps + 1


s = Solution()
print ("hERE")
s.climbStairs(45)
