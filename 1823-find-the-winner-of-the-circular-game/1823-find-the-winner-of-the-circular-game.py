class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        f=range(1,n+1)
        i=0
        c=1
        while len(f)> 1:
            if c==k:
                f.pop(i)
                c=1
            else:
                c+=1
                i=(i+1)%len(f)
        return f[0]        
                
            
            