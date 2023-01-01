class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        idx = -1
        size = len(points)
        min_distance = -1
        for i in range(size):
            x1 = points[i][0]
            y1 = points[i][1]
            
            if x1 == x or y1 == y:
                cur_distance = abs(x1 - x) + abs(y1 - y)
                if min_distance == -1:
                    min_distance = abs(x1 - x) + abs(y1 - y) 
                    idx = i   
                
                elif cur_distance < min_distance:
                    min_distance = cur_distance
                    idx = i
                    
        return idx