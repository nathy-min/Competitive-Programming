class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        good_pairs = 0
        for i in range(size-1):
            for j in range(i+1, size):
                if nums[i] == nums[j]:
                    good_pairs += 1
                    
        return good_pairs            
            