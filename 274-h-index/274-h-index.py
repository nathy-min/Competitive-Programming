class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        s=sorted(citations)[::-1]
        i=0
        c=0
        while i<len(s) and s[i]>=i+1:
            c+=1
            i+=1
        return c    