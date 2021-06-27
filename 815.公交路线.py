class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        n = len(routes)
        edges = [[False for _ in range(n)] for _ in range(n)]
        rec = collections.defaultdict(list)
        recd = collections.defaultdict(set)

        for i in range(n):
            route = routes[i]
            for site in route:
                for x in rec[site]:
                    edges[x][i] = edges[i][x] = True
                rec[site].append(i)
                recd[i].add(site)
        step = 1
        q = deque()
        seen = set()
        for x in rec[source]:
            q.append(x)
            seen.add(x)
        
        while q:
            for _ in range(len(q), 0, -1):
                cur = q.popleft()
                if target in recd[cur]:
                    return step
                for dst in range(n):
                    if dst not in seen and edges[cur][dst]:
                        seen.add(dst)
                        q.append(dst)
            step += 1
        return -1
