class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.children[ord(c) - 97]:
                curr.children[ord(c) - 97] = TrieNode()
            curr = curr.children[ord(c) - 97]
        curr.is_end += 1  

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        for word in words:
            self.addWord(word)
        self.count = 0

        def dfs(j, node):
            if j >= len(s):
                return

            curr = node
            for i in range(26):
                child = curr.children[i]
                if child:
                    idx = -1
                    for a in range(j, len(s)):
                        if s[a] == chr(i + 97):
                            idx = a
                            break
                    if idx != -1:
                        self.count += child.is_end
                        dfs(idx + 1, child)
                        
                        

        dfs(0, self.root)                     
        return self.count            

class TrieNode:
    def __init__(self):
        self.is_end = 0
        self.children = [None for _ in range(26)]