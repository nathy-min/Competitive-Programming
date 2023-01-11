class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = [i+1 for i in range(n)]
        ptr = 0
        while len(lst) > 1:
            ptr = (ptr + (k - 1)) % len(lst) 
            lst.pop(ptr)
        return lst[0]     
            