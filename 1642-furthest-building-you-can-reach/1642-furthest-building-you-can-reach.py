class Solution(object):
    def furthestBuilding(self, A, bricks, ladders):
        heap=[]
        for i in range(len(A)-1):
            h=A[i+1]-A[i]
            if h <= 0:
                continue
            heapq.heappush(heap,h)
            if len(heap)> ladders:
                p= heapq.heappop(heap)
                bricks -= p
            if bricks<0:
                return i
        return len(A)-1    
            
        
        