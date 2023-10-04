class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])

        q = deque()
        ans = []
        for lst in queries:
            q = deque()
            visited = set()
            q.append(lst[1])
            flag = False
            while q:
                num = q.popleft()
                if num and num in visited:
                    continue
                if num == lst[0]:
                    flag = True
                    break
                visited.add(num)

                    
                for parent in graph[num]:                    
                    q.append(parent)
            ans.append(flag)

        return ans