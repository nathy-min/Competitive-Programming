class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        no_col = 0
        size = len(strs[0])
        
        for i in range(size):
            temp = [word[i] for word in strs]
            sorted_temp = sorted(temp)
            if sorted_temp != temp:
                no_col += 1
                
        return no_col