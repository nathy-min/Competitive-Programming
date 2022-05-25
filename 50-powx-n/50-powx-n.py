class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def power(x,n):
            if x == 0 : return 0
            if n==0 : return 1
            
            ans = power(x,n//2)
            ans = ans * ans
            return x*ans if n%2 else ans
        ans = power(x,abs(n))
        return ans if n>= 0 else 1/ans