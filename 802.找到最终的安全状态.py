class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(x):
            if color[x] > 0:
                return color[x] == 2

            color[x] = 1
            for v in graph[x]:
                if not dfs(v):
                    return False
            color[x] = 2
            return True

        n = len(graph)
        color = [0] * n
        return [i for i in range(n) if dfs(i)]


