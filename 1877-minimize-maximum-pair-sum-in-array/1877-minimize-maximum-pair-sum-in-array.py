class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        nums.sort()
        i,j=0,len(nums)-1
        while j>i:
            a=max(nums[i]+nums[j],a)
            i+=1
            j-=1
        return a