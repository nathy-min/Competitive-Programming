class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        size = len(words)
        
        for i in range(size - 1):
            ptr = 0
            while ptr < len(words[i]) and ptr < len(words[i+1]):
                idx1 = order.index(words[i][ptr])
                idx2 = order.index(words[i+1][ptr])
                
                if idx1 > idx2 :
                    return False
                
                if idx1 == idx2:
                    ptr += 1
                    
                if idx1 < idx2:
                    break
                    
                if ptr == len(words[i]) - 1 or ptr == len(words[i+1]):
                    if len(words[i]) > len(words[i+1]):
                        return False
                    
        return True            