class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            fib=[0,1]
            i=1
            while i<n:
                fib.append(sum(fib))
                fib.pop(0)
                i+=1
            return fib[-1]
            