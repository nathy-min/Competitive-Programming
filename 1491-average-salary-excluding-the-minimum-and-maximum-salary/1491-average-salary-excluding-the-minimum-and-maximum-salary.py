class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        size = len(salary)
        sum_salary = float(sum(salary[1:size-1]))
        avg_salary = sum_salary /(size - 2)
        
        return avg_salary