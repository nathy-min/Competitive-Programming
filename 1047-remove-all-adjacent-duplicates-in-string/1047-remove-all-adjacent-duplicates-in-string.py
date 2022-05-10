class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        li=[]
        li[:0]=s
        i=0
        j=1
        while li and j!= len(li):
            
            if li[i]==li[j]:
                li.pop(i)
                li.pop(j-1)
                if i==0:
                    continue
                else:
                    i-=1
                    j-=1
            else:
                i+=1
                j+=1
        S=''
        return S.join(li)
                    