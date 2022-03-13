class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        ch=sorted(changed)
        a=len(ch)/2
        if len(ch)%2==1 or 2*ch[0]>ch[-1]:
            return []

        i=0
        j=1
        while j<len(ch):
            if 2*ch[i]>ch[j]:

                j+=1
                if j==len(ch):
                    return []
            elif 2*ch[i]==ch[j]:
                ch.pop(j)
                i+=1
                if i==j:
                    j+=1
            else:
                return []
        if len(ch)!=a:
            return []
        return ch