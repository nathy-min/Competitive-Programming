class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    a[i]+=1
        return a            