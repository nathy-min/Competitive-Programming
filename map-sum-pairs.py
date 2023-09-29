class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for c in key:
            child = (ord(c) - 97)
            if not curr.children[child]:
                curr.children[child] = TrieNode()
            curr = curr.children[child]

        curr.v = val
        print(curr.v, val)

    def sum(self, prefix: str) -> int:
        curr = self.root
        self.count = 0
        for s in prefix:
            child = (ord(s) - 97)
            if not curr.children[child]:
                return 0
            curr = curr.children[child]

        def dfs(node):
                self.count += node.v
                for child in node.children:
                    if child:
                        dfs(child)

        dfs(curr)
        return self.count            



        
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.v = 0

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)