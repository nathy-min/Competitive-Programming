class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com_pre = ''
        i = 0 
        
        while i < len(strs[0]):
            breaker = False
            for j in range(len(strs) - 1):
                nxt_len = len(strs[j + 1])
                if nxt_len <= i :
                    breaker = True
                    break
                if  strs[j][i] != strs[j + 1][i]:
                    breaker = True
                    break
            if breaker:
                break
            com_pre += strs[0][i]  
            i += 1  

        return com_pre   
