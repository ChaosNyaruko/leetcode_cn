class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in times:
            g[u - 1].append((v - 1, w))

        q = [(0, k - 1)]
        dist = [float('inf') for _ in range(n)]
        dist[k - 1] = 0
        while q:
            w, u = heapq.heappop(q)
            if dist[u] < w:
                continue

            for v, w in g[u]:
                if (d:=dist[u] + w) < dist[v]:
                    heapq.heappush(q, (d, v))
                    dist[v] = d
        res = max(dist)
        return res if res < float('inf') else -1




