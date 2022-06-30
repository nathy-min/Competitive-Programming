class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        y1 = (points[1][1] - points[0][1])
        x1 = (points[1][0] - points [0][0])
        y2 = (points[2][1] - points[1][1])
        x2 = (points[2][0] - points [1][0])

        if y1*x2 != y2*x1:
            return True
        return False