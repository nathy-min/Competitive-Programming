class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        res = [False] * len(l)
        for i in range(len(l)):
            seq = sorted(nums[l[i]: r[i] + 1])
            if len(seq) <= 2:
                res[i] = True
            else:
                isArithmetic = True
                diff = seq[1] - seq[0]
                for j in range(1, len(seq) - 1):
                    if seq[j + 1] - seq[j] != diff:
                        isArithmetic = False
                        break
                if isArithmetic:
                    res[i] = True
        return res