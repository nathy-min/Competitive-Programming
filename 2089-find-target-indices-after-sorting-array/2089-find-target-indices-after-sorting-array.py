class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    m=nums[i]
                    nums[i]=nums[j]
                    nums[j]=m
        for i in range(len(nums)):
            if nums[i]== target:
                a.append(i)
        return a        