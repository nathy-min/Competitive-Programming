class Solution:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        curr = self.root
        for c in word:
            child = (ord(c) - 97)
            if not curr.children[child]:
                curr.children[child] = TrieNode()
            curr = curr.children[child]
        curr.is_end = True 

    def longestWord(self, words: List[str]) -> str:
        curr = self.root
        self.longest_word = ''
        
        def dfs(node, string):
            for i in range(26):
                if node.children[i] and node.children[i].is_end:
                    ch = chr(i + 97)
                    temp = string
                    string += ch
                    if not self.longest_word or (len(string) > len(self.longest_word)):
                        self.longest_word = string
   
                    dfs(node.children[i], string)
                    string = temp

        for word in words:
            self.insert(word)
        dfs(curr, '')    
        return self.longest_word


class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False