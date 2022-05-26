class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def helper(n):
            if n == 1: return '0'
            ans = helper(n-1)
            res = ''
            for i in ans:
                if i == '0': res += '1'
                else: res +='0'
            ans += '1' + res[::-1]
            return ans
        ans = helper (n)    
        return ans[k-1]    