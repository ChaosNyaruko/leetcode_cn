#
# @lc app=leetcode.cn id=959 lang=python3
#
# [959] 由斜杠划分区域
#
# https://leetcode-cn.com/problems/regions-cut-by-slashes/description/
#
# algorithms
# Medium (68.42%)
# Likes:    138
# Dislikes: 0
# Total Accepted:    5.6K
# Total Submissions: 7.9K
# Testcase Example:  '[" /","/ "]'
#
# 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。
# 
# （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
# 
# 返回区域的数目。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：
# [
# " /",
# "/ "
# ]
# 输出：2
# 解释：2x2 网格如下：
# 
# 
# 示例 2：
# 
# 输入：
# [
# " /",
# "  "
# ]
# 输出：1
# 解释：2x2 网格如下：
# 
# 
# 示例 3：
# 
# 输入：
# [
# "\\/",
# "/\\"
# ]
# 输出：4
# 解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
# 2x2 网格如下：
# 
# 
# 示例 4：
# 
# 输入：
# [
# "/\\",
# "\\/"
# ]
# 输出：5
# 解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
# 2x2 网格如下：
# 
# 
# 示例 5：
# 
# 输入：
# [
# "//",
# "/ "
# ]
# 输出：3
# 解释：2x2 网格如下：
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length == grid[0].length <= 30
# grid[i][j] 是 '/'、'\'、或 ' '。
# 
# 
#

# @lc code=start
class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.count = n
        self.size = [1] * n
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.size[rx] < self.size[ry]:
            ry, rx = rx, ry
        self.parents[ry] = rx
        self.size[rx] += self.size[ry]
        self.count -= 1
        return

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        def g(i, j, k):
            return (i * n + j) * 4 + k
        uf = UnionFind(n * n * 4)
        for i in range(n):
            for j in range(n):
                if i > 0:
                    uf.union(g(i - 1, j, 1), g(i, j, 3))
                if j > 0:
                    uf.union(g(i, j - 1, 0), g(i, j, 2))
                if grid[i][j] != '/':
                    uf.union(g(i, j, 0), g(i, j, 3))
                    uf.union(g(i, j, 1), g(i, j, 2))
                if grid[i][j] != '\\':
                    uf.union(g(i, j, 2), g(i, j, 3))
                    uf.union(g(i, j, 0), g(i, j, 1))
        return uf.count

        
# @lc code=end

