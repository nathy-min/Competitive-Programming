class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        df = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                df[word[:i] + "*" + word[i+1:]].append(word)
                
        visited = set()
        visited.add(beginWord)
        queue = collections.deque([(beginWord, 1)])
        
        
        while queue:
            node, lvl = queue.popleft()
            for i in range(len(node)):
                for x in df[node[:i] + "*" + node[i+1:]]:  
                    if x == endWord:
                        return lvl+1
                    if x not in visited:
                        visited.add(x)
                        queue.append((x, lvl+1) )
        return 0