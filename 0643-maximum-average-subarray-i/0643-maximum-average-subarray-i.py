class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
           
        current=0
        for i  in range(k) :
            current+=nums[i]
        maxi = current
        for i in range(k,len(nums)) :
            current+=nums[i]-nums[i-k]
            maxi = max(current,maxi)
        return maxi/k