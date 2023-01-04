class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        size = len(nums)
        
        for i in range(size):
            ans.append(nums[nums[i]])
            
        return ans    