class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        row,col = len(matrix),len(matrix[0]) 
        self.mat=[[0]*(col+1) for i in range (row+1)]
        for r in range(row):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                above = self.mat[r][c+1]
                self.mat[r+1][c+1] = above + prefix
                
                

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        
        r1,c1,r2,c2 = row1+1,col1+1,row2+1,col2+1
        br= self.mat[r2][c2]
        ab= self.mat[r1-1][c2]
        l= self.mat[r2][c1-1]
        ul= self.mat[r1-1][c1-1]
        summation = br - ab - l + ul 
        return summation
           
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)