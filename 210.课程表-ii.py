#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        for edge in prerequisites:
            edges[edge[1]].append(edge[0])
        
        visited = [0] * numCourses
        res = []
        valid = True
        def dfs(u):
            nonlocal valid
            visited[u] = 1            
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    # looped
                    valid = False
                    return
            res.append(u)
            visited[u] = 2
        for i in range(numCourses):
            if valid and visited[i] == 0:
                dfs(i)
        if not valid:
            return list()
        return res[::-1]

            
# @lc code=end

