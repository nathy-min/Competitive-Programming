class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def binarySearch(start,end):
            if start == end:
                return start
            mid = (start+end)//2
            if totalTrips > (sum(mid//x for x in time)):
                return binarySearch(mid+1,end)
            return binarySearch(start,mid)
        return binarySearch(1,min(time)*totalTrips)
