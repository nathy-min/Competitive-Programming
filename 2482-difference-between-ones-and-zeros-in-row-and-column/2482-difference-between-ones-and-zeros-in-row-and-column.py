class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        row_ones = []
        row_zeros = []
        col_ones = []
        col_zeros = []
        rows = len(grid)
        cols = len(grid[0])
        result = [ [0 for _ in range(cols)] for _ in  range(rows)]
        
        for i in range(rows):
            row_ones.append(grid[i].count(1))
            row_zeros.append(cols - row_ones[-1])
            
        for i in range(cols):
            count = 0
            for j in range(rows):
                if grid[j][i] == 1:
                    count += 1
            col_ones.append(count)
            col_zeros.append(rows - col_ones[-1])
        
        for i in range(rows):
            for j in range(cols):
                result[i][j] = row_ones[i] + col_ones[j] - row_zeros[i] - col_zeros[j]

        return result
            