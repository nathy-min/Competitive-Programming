class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r = len(grid) - 1
        c = 0
        count = 0
        while r >=0 and c < len(grid[0]):
            if grid[r][c] >= 0:
                c += 1
            else:
                count += len(grid[0]) - c
                r -= 1
        return count