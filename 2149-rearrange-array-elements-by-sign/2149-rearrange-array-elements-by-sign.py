class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=[0]*len(nums)
        p=0
        n=1
        for i in nums:
            if i>0:
                a[p]=i
                p+=2
            else:
                a[n]=i
                n+=2
        return a
        