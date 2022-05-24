class Solution(object):
    def PredictTheWinner(self, nums):
        def can_maximize_score(nums, p, q):
            if len(nums) == 1:
                p += nums[0]
                return p >= q
            elif len(nums) == 2:
                p += nums[0] if nums[0] >= nums[1] else nums[1]
                q += nums[1] if nums[1] < nums[0] else nums[0]
                return p >= q
            else:
                option1 = can_maximize_score(nums[1:-1], p + nums[0], q + nums[-1])
                option2 = can_maximize_score(nums[2:], p + nums[0], q + nums[1])
                option3 = can_maximize_score(nums[1:-1], p + nums[-1], q + nums[0])
                option4 = can_maximize_score(nums[:-2], p + nums[-1], q + nums[-2])
                if option1 and option2 or option3 and option4:
                    return True
                return False
            
        return can_maximize_score(nums, 0, 0)