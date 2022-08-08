class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)>1:
            stones=[-i for i in stones]
        else: return stones[0]    
        heapq.heapify(stones)
        print (stones)
        while len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if y>x:
                heapq.heappush(stones,-(y-x))
            print (stones)    
        if stones: return -stones[0]
        return 0