class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        order = [[0 for _ in range(n)] for _ in range(n)]

        match = [0 for _ in range(n)]
        for x,y in pairs:
            match[x] = y
            match[y] = x
        
        for i in range(n):
            for j in range(n - 1):
                order[i][preferences[i][j]] = j

        res = 0
        for x in range(n):
            y = match[x]
            yIndex = order[x][y]
            for i in range(yIndex):
                u = preferences[x][i]
                v = match[u]
                if order[u][x] < order[u][v]:
                    res += 1
                    break
        
        return res
