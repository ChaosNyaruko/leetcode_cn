#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        for i in range(1, n + 1):
            parent[i] = i
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(x, y):
            parent[find(x)] = find(y)
        
        for edge in edges:
            a, b = edge[0], edge[1]
            if find(a) != find(b):
                union(a, b)
            else:
                return edge
        return []
        
# @lc code=end

