class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        res = -1
        l = 1
        r = max(nums)
        def logic(div):
            num = 0
            for i in nums:
                num += (-(-i//div))
            return num
        while l <= r:
            m = (r + l)//2
            if logic(m) > threshold:
                l = m + 1
            else:
                res = m
                r = m - 1
        return res