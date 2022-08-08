class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        for r in range(len(matrix)):
            heapq.heappush(h,(matrix[r][0],r,0))
        while k > 1:
            val,r,c = heapq.heappop(h)
            if c+1 < len(matrix):
                heapq.heappush(h,(matrix[r][c+1],r,c+1))
            k-=1
        return heapq.heappop(h)[0]