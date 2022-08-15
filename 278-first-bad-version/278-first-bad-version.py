# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        badver = float("-inf")
        l = 1
        r = n
        while l <= r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        return l