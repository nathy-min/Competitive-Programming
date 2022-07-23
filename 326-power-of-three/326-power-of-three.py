class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=1:
            return n==1 or n==-1
        else:
            
            return self.isPowerOfThree(n/3)