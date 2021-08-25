class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]
        n = len(graph)
        res = []
        def dfs(u):
            if u == n - 1:
                res.append(path.copy())
                return

            for v in graph[u]:
                # print(u, "->", v)
                path.append(v)
                dfs(v)
                path.pop()

        dfs(0)
        return res

