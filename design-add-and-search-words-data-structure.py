class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.children[ord(c) - 97]:
                curr.children[ord(c) - 97] = TrieNode()
            curr = curr.children[ord(c) - 97]
        curr.is_end = True        

    def search(self, word: str) -> bool:
        def dfs(j, node):    
            curr = node
            for i in range(j, len(word)):
                if word[i] == '.' :
                    for child in curr.children:
                        if child:
                            if dfs(i + 1, child): 
                                return True
                    return False        
                else:
                    if not curr.children[ord(word[i]) - 97]:
                        return False
                    curr = curr.children[ord(word[i]) - 97]
            return curr.is_end            

        return dfs(0, self.root)
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)