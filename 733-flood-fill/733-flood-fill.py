class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols = len(image),len(image[0])
        curC=image[sr][sc]
        def dfs(r,c):
            if 0<=r<rows and 0<=c<cols and image[r][c] == curC and image[r][c]!=color:
                image[r][c] = color
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        dfs(sr,sc)        
        
        return image