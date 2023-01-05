class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dic = defaultdict(int)
        no_pair = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            dic[tuple(grid[i])] += 1
            
        for j in range(cols):
            temp_tupel = tuple([row[j] for row in grid])
            no_pair += dic[temp_tupel]
            
        return no_pair    