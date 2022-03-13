class Solution(object):    
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        l,r=0,len(nums)-1
        result=[]
        for i in range(len(nums)//2):
            result.append(nums[l])
            result.append(nums[r])
            l+=1
            r-=1
            if l==r:
                result.append(nums[l])
                                
        return result         