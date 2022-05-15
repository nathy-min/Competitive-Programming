class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[-1]*len(nums1)
        dicn1={i:v for v,i in enumerate(nums1)}
        stack=[]
        for i in nums2:
            while stack and i>stack[-1]:
                ans[dicn1[stack.pop()]]=i
            if i in nums1:
                stack.append(i)
                
        return ans