class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        size = len(nums)
        
        for i in range(size - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                
        write = 0
        read = 0
        while read < len(nums):
            if nums[read] != 0:
                temp = nums[read]
                nums[read] = nums[write]
                nums[write] = temp
                write = write + 1
            read = read + 1
            
        return nums    
      
        