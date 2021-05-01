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
        res = 0
        mp = {employee.id: employee for employee in employees}
        q = deque([id])
        while q:
            e = mp[q.popleft()]
            res += e.importance
            for i in e.subordinates:
                q.append(i)
        
        return res
