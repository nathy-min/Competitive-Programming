class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = 0
        """    
        while x!=0:
            d = x % 10
            y = y * 10 + d
            x //= 10
"""
        y = str(x)[::-1]
        return (y == str(x))
