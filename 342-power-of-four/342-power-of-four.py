class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x=4
        while x<n:
            x*=4
        return x==n or n==1    