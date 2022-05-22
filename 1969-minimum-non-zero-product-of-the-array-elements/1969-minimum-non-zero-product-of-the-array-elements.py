class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        modulo = 10 **9 + 7

        max_num = pow(2, p, modulo) - 1
        common_multiple = max_num - 1
        exp = pow(2, p-1) - 1
        return (pow(common_multiple, exp, modulo) * max_num) % modulo