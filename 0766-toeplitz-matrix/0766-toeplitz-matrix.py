class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        
        bool_value = all(matrix[r][:-1] == matrix[r + 1][1:] for r in range(rows - 1))
        return bool_value