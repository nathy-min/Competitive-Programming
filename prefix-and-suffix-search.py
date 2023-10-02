class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.words = words
        for index,word in enumerate(words):
            temp = word + '#' + word
            n = len(word)
            for i in range(n):
                self.insert(temp[i:], index)

    def insert(self, word, index):
        curr = self.root
        curr.index = index
        for c in word:          
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.index = index     
        
    def f(self, pref: str, suff: str) -> int:
        curr = self.root
        
        ps = suff + '#' + pref
        for c in ps:
            if c not in curr.children:
                return -1
            curr = curr.children[c]    
        return curr.index        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)