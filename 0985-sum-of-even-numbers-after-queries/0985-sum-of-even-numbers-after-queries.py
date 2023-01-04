class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        size_que = len(queries)
        size_nums = len(nums)
        answer = []
        sum_even = 0
        
        for i in range(size_nums):
            if nums[i] % 2:
                continue
            else:
                sum_even += nums[i]
        for i in range(size_que):
            indx = queries[i][1]
            prev_value = nums[indx]
            nums[indx] += queries[i][0]
            if nums[indx] % 2 == 0:
                if prev_value % 2 != 0:
                    sum_even += nums[indx]
                else:
                    sum_even += queries[i][0]
            else:
                if prev_value % 2 == 0:
                    sum_even -= prev_value
                
            answer.append(sum_even)
            
        return answer
              
            
            
            
        