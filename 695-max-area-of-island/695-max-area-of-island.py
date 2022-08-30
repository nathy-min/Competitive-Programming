class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        maxa = 0
        visit = set()
        def dfs(r,c):
            if r == rows or c == cols or r < 0 or c < 0 or (r,c) in visit or grid[r][c] != 1:
                return 0
            visit.add((r,c))
            res = 0
            for r1,c1 in [(1,0),(-1,0),(0,1),(0,-1)]:
                res += dfs(r + r1,c + c1)
            return res + 1
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit and grid[i][j] == 1:
                    maxa = max(dfs(i,j),maxa)
        return maxa
        