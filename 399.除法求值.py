#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = collections.defaultdict(list)
        edgesWithValue = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            edges[eq[0]].append(eq[1])
            edges[eq[1]].append(eq[0])
            edgesWithValue[eq[0]].append(values[i])
            edgesWithValue[eq[1]].append(1.0/values[i])

        # print("edges", edges)
        # print("edgesWithValue", edgesWithValue)
        def dfs(start, end, curValue, visited):
            if start in visited and visited[start] == True: 
                return -1
            if start not in edges:
                return -1
            if start == end:
                return curValue
            
            visited[start] = True
            tmp = -1
            for i, target in enumerate(edges[start]):
                tmp = dfs(target, end, curValue * edgesWithValue[start][i], visited)
                if tmp != -1:
                    break
            visited[start] = False
            return tmp
        res = []
        for query in queries:
            visited = dict()
            res.append(dfs(query[0], query[1], 1.0, visited))


        return res 
# @lc code=end

