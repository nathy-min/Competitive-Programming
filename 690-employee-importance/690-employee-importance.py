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
        imp={}
        sub={}
        for emp in employees:
            imp[emp.id] = emp.importance
            sub[emp.id] = emp.subordinates
        
        def dfs(id):
            total_imp = imp[id]
            for s in sub[id]:
                total_imp += dfs(s)
            return total_imp
        return dfs(id)
            