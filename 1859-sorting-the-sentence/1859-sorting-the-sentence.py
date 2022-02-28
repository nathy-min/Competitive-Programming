class Solution:
    def sortSentence(self, s: str) -> str:
             l = s.split(' ')
        
             ll = []
        
             for w in l:
                ll.append([w[-1], w[:-1]])
        
             ll.sort(key = lambda x: x[0])
        
             return ' '.join([word[1] for word in ll])