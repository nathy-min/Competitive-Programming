class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        nums.sort()
        if size in nums:
            missing_value = 0
        else:
            missing_value = size
        ptr = 0
        print(nums)
        if size == 1:
            if nums[0] == 0:
                return 1
            else:
                return 0
        while ptr < size - 1:
            if nums[ptr] != nums[ptr + 1] - 1:
                missing_value = nums[ptr] + 1
                break
            else:
                ptr += 1
                
        return missing_value        
            
                