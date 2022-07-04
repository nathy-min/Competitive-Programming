class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        result = 0
        
        for i in range(0, len(nums) - firstLen -secondLen + 1):
            sub1 = sum(nums[i:i+firstLen])
            for j in range(i + firstLen, len(nums) - secondLen + 1):
                total_sum = sum(nums[j:j+secondLen]) + sub1
                if total_sum > result: 
                    result = total_sum
                    
        nums.reverse()
        
        for i in range(0, len(nums) - firstLen - secondLen + 1):
            sub1 = sum(nums[i:i+firstLen])
            for j in range(i +firstLen, len(nums) - secondLen + 1):
                total_sum = sum(nums[j:j+secondLen]) + sub1
                if total_sum > result: 
                    result = total_sum           
        
        return result