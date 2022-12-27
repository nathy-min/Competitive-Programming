class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        remainder = n % 2
        if remainder:
            result = n*2
        else:
            result = n
        return result        
