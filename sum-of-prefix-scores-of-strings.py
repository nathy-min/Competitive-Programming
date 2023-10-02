class TrieNode:
    
    def __init__(self) -> None:
        self.vstd = 0
        self.children = {}


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = TrieNode()
        ans = []        
        
        def addWord(word: str) -> None:
            curr = trie
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
                curr.vstd +=1
            
        
        def calcScore(word: str) -> int:
            score = 0
            curr = trie
            
            for c in word:
                curr = curr.children[c]
                score += curr.vstd
            return score
        
        
        for word in words:
            addWord(word)
            
        for word in words:
            score = calcScore(word)
            ans.append(score)
        
        return ans