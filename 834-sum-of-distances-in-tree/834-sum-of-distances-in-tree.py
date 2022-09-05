class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        df = defaultdict(list)

        for a,b in edges:
            df[a].append(b)
            df[b].append(a)

        count = [0]*n
        ans = [0]*n
        visited = set()

        def dfs(curr_child):
            nonlocal count,ans
            nodes = 1

            for c in df[curr_child]:
                if c not in visited:
                    visited.add(c)
                    child_nodes = dfs(c)
                    nodes += child_nodes
                    ans[0] += child_nodes

            count[curr_child] = nodes
            return nodes
        visited.add(0)
        dfs(0)

        def count_dfs(curr_child):
            nonlocal ans
            for c in df[curr_child]:
                if c not in visited:
                    visited.add(c)
                    ans[c] = ans[curr_child] - count[c] + (n - count[c])
                    count_dfs(c)

        visited = set()
        visited.add(0)
        count_dfs(0)

        return ans