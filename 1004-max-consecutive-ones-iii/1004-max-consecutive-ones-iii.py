class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mc=0
        c=0
        s=0
        for end in range(s,len(nums)):
            if nums[end]==0:
                c+=1
                
            while(c>k):
                if nums[s]==0:
                    c-=1
                s+=1
            mc=max(mc,end-s+1)
        return mc       