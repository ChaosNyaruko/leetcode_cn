#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
# https://leetcode-cn.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (64.22%)
# Likes:    401
# Dislikes: 0
# Total Accepted:    68.3K
# Total Submissions: 106.3K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。
# 
# 一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被
# 0（代表水）包围着。
# 
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
# 
# 
# 
# 示例 1:
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# 
# 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
# 
# 示例 2:
# 
# [[0,0,0,0,0,0,0,0]]
# 
# 对于上面这个给定的矩阵, 返回 0。
# 
# 
# 
# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。
# 
#

# @lc code=start
class Solution:
    def dfs(self, grid, x, y) -> int:
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return 0
        if grid[x][y] == 0:
            return 0
        grid[x][y] = 0
        ans = 1
        ans += self.dfs(grid, x - 1, y)
        ans += self.dfs(grid, x + 1, y)
        ans += self.dfs(grid, x , y + 1) 
        ans += self.dfs(grid, x, y - 1)
        return ans
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        res = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    res = max(res, self.dfs(grid, x, y))
                    # res += self.dfs(grid, x, y)
        return res

        
# @lc code=end

