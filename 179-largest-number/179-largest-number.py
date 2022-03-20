class Solution:
    def comparator(self, num1, num2):
        if str(num1) + str(num2) > str(num2) + str(num1):
            return -1
        elif str(num1) + str(num2) < str(num2) + str(num1):
            return 1
        else:
            return 0

    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(self.comparator))
        no_of_zeros = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                no_of_zeros += 1
            else:
                break
        if no_of_zeros == len(nums):
            return "0"
        return "".join([str(num) for num in nums])  