class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        pairs = 0
        size = len(words)
        
        for i in range(size):
            set1 = set(words[i])
            for j in range(i + 1 , size):
                set2 = set(words[j])
                if set1.issubset(set2) and set2.issubset(set1):
                    pairs += 1
                 
        return pairs        