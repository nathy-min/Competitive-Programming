class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        zeros = [0]*(1 +len(matrix[0]))
        self.matrix = matrix  
        self.matrix.insert(0,zeros)
        print(self.matrix)
        for row in self.matrix[1:]:
            row.insert(0,0)
            
        for row in range(1,len(self.matrix)):
            for col in range(1,len(self.matrix[row])):
                self.matrix[row][col] = self.matrix[row][col] + self.matrix[row - 1][col] + self.matrix[row][col - 1] - self.matrix[row - 1][col - 1]
                
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        ans = self.matrix[row2][col2] - self.matrix[row1 - 1][col2] - self.matrix[row2][col1 - 1] + self.matrix[row1 - 1][col1 - 1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)