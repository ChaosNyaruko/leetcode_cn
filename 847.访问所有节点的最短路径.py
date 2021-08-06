class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque()
        for i in range(n):
            q.append((i, 1 << i, 0))

        seen = set()
        ans = 0
        while q:
            cur = q.popleft()
            if cur[1] == (1 << n) - 1:
                ans = cur[2]
                break
            for v in graph[cur[0]]:
                status = cur[1] | (1 << v)
                if (v, status) not in seen:
                    seen.add((v, status))
                    q.append((v, status, cur[2] + 1))

        return ans
