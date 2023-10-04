class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        weights = {}
        for i in range(1, n + 1):
            weights[i] = float('inf')
        weights[k] = 0    

        for path in times:
            graph[path[0]].append((path[1], path[2]))

        heap = [[0, k]]       
        visited = set()

        while heap:
            w, v = heapq.heappop(heap)
            if v in visited:
                continue
            visited.add(v)

            for node, weight in graph[v]:
                temp = weight + weights[v]
                if weights[node] > temp:
                    weights[node] = temp
                    heapq.heappush(heap, [temp, node])

        ans = 0
        for val in weights.values():
            if val == float('inf'):
                return -1
            ans = max(ans, val)

        return ans