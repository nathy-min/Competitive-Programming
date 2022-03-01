class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        rtype=[]
        d={}
        a=s.split(' ')
        for l in a:
            d[l[-1]]=l[:-1]
        for i in range(1,len(d)+1):
            b=str(i)
            rtype.append(d[b])
        
        return(' '.join(rtype))