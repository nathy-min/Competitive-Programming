class Solution(object):
    def largestPerimeter(self, nums):
        num = sorted(nums)
        num.reverse()
        max_perimeter  = 0
        ptr = 2
        print(num)
        size = len(num)
        
        while max_perimeter == 0 and ptr < size:
            side1 = num[ptr - 2]
            side2 = num[ptr]
            side3 = num[ptr - 1]
            if side2 + side3 > side1:
                max_perimeter = side1+side2+side3
            ptr += 1
            
        return max_perimeter 
        