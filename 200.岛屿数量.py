#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (51.35%)
# Likes:    888
# Dislikes: 0
# Total Accepted:    183.3K
# Total Submissions: 356.8K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# grid[i][j] 的值为 '0' 或 '1'
# 
# 
#

# @lc code=start
class Solution:
    def dfs(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return
        if grid[x][y] == '0':
            return
        grid[x][y] = '0'
        self.dfs(grid, x+1, y)
        self.dfs(grid, x - 1, y)
        self.dfs(grid ,x , y + 1)
        self.dfs(grid, x, y - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0

        cnt = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    self.dfs(grid, x, y)
                    cnt += 1
        return cnt
# @lc code=end

