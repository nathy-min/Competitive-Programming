class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i,j=0,len(nums)-1
        c=0
        while j>i:
            total=nums[i]+nums[j]
            if total==k:
                i+=1
                j-=1
                c+=1
            elif total>k:
                j-=1
            else:
                i+=1
                
            
            
                
        return c               