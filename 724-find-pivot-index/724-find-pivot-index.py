class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            rightsum = total - nums[i] - leftsum
            if rightsum == leftsum:
                return i
            leftsum += nums[i]
        return -1    