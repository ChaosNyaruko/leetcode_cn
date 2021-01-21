#
# @lc app=leetcode.cn id=1489 lang=python3
#
# [1489] 找到最小生成树里的关键边和伪关键边
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.size = [1] * n
        self.connectCount = n
        self.parent = list(range(n))
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        self.connectCount -= 1
        return True
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key = lambda x: x[2]) # sort by weight

        uf_std = UnionFind(n)
        value = 0
        for i in range(m):
            if uf_std.union(edges[i][0], edges[i][1]):
                value += edges[i][2]


        res = [list(), list()]

        for i in range(m):
            # 判断是否是关键边
            uf = UnionFind(n)
            v = 0
            for j in range(m):
                if i != j and uf.union(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if uf.connectCount != 1 or v > value:
                res[0].append(edges[i][3])
                continue

            # 判断是否是伪关键边
            uf = UnionFind(n)
            uf.union(edges[i][0], edges[i][1])
            # 题目已说明这是一个连通图，先考虑edges[i]也一定形成生成树(不一定最小)
            v = edges[i][2]
            for j in range(m):
                if i != j and uf.union(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if v == value:
                res[1].append(edges[i][3])

        return res
# @lc code=end

