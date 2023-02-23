class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runingsum = [0]
        for i in range(len(nums)):
            runingsum.append(runingsum[-1] + nums[i])
            
        return runingsum[1:]    