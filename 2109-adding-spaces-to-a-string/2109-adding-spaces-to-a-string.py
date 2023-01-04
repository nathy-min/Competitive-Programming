class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        res= []
        i, j= 0, 0
        
        while i < len(s):
            if j < len(spaces) and spaces[j] == i:
                res.append(' ')
                j+=1
            else:
                res.append(s[i])
                i+=1
            
        return ''.join(res)