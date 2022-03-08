class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        points.sort(key=lambda x:x[0]**2+x[1]**2)
       
        return points[:k]   