class NumArray:

    def __init__(self, nums: List[int]):
        self.pref_sum = nums
        for i in range(1 , len(self.pref_sum)):
            self.pref_sum[i] += self.pref_sum[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.pref_sum[right] - self.pref_sum[left - 1]
        return self.pref_sum[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)