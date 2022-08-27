"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj = defaultdict(list)
        for emp in employees:
            adj[emp.id] = (emp.importance,emp.subordinates)
        def dfs(eid):
            val = 0
            for i in adj[eid][1]:
                val += dfs(i)
            return val + adj[eid][0]
        return dfs(id)