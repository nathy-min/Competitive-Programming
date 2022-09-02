class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        res = 0
        def dfs(r,c):
            direction = [[0,1],[0,-1],[1,0],[-1,0]]
            if 0 <= r < rows and  0<=c<cols and grid[r][c] == 1:
                grid[r][c] = -1
                for i,j in direction:
                    dfs(r + i,c + j)
        for i in range(cols):
            for j in [0,rows - 1 ]:
                dfs(j,i)
        
        for i in range(rows):
            for j in [0, cols - 1]:
                dfs(i,j)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res += 1
        return res
    