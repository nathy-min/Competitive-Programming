class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c=Counter(nums)
        output=[]
        n=0
        for j,v in sorted(c.items(),key=lambda x: -x[1]):
            output.append(j)
            n+=1
            if n==k: break
                
        return output        