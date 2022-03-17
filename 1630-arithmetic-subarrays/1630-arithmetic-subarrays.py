class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        subs=[]
        bol=[]
        result=[]
        for i in range(len(l)):
            subs=sorted(nums[l[i]: r[i]+1])
            if len(subs)==0 or len(subs)==1:
                result.append(False)
                continue
                
            elif len(subs)==2:
                result.append(True)
                continue
            else:
                
                for a in range(2,r[i]-l[i]+1):
                    sub=subs[1]-subs[0]
                    
                    if subs[a]-subs[a-1]==sub:
                        bol.append(True)
                    else:
                        bol.append(False)
                if False in bol:
                    result.append(False)
                else:
                    result.append(True)
                bol=[]   
        return result