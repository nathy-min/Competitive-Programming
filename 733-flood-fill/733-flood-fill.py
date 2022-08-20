class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols = len(image),len(image[0])
        def dfs(r,c):
            nonlocal stpx
            if r == rows or r < 0 or c == cols or c < 0 or image[r][c] != stpx or (r,c) in visited:
                return
            image[r][c] = color
            visited.add((r,c))
            dirn = [[1,0],[-1,0],[0,1],[0,-1]]
            for i,j in dirn:
                dfs(r +i,c + j)
        visited = set()
        
        stpx = image[sr][sc]
        dfs(sr,sc)
        
        return image