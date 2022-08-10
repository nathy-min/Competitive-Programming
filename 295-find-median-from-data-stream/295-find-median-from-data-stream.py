class MedianFinder:

    def __init__(self):
        self.smol = []
        self.large = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.smol, -num)
        if self.smol and self.large and -self.smol[0] > self.large[0]:
            heapq.heappush(self.large,-heapq.heappop(self.smol))
        if len(self.smol)  > len(self.large) + 1:
            heapq.heappush(self.large,-heapq.heappop(self.smol))
        if len(self.large) > len(self.smol) + 1:
            heapq.heappush(self.smol,-heapq.heappop(self.large))
    def findMedian(self) -> float:
        sdif = len(self.smol) - len(self.large)
        print(sdif)
        # Trust it'll be valid
        if sdif == 0: return (-self.smol[0] + self.large[0] )/ 2
        return -self.smol[0] if sdif >= 1 else self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()