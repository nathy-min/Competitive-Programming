class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        def dfs(x):
            for i, connected in enumerate(isConnected[x]):
                if connected and i not in seen:
                    seen.add(i)
                    dfs(i)
        count = 0
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
                
        return count