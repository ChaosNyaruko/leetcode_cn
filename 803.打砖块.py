#
# @lc app=leetcode.cn id=803 lang=python3
#
# [803] 打砖块
#

# @lc code=start
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        # mark connected nodes
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            res = 1
            grid[i][j] = 2
            res += sum(dfs(x, y) for x, y in [(i-1, j), (i + 1, j), (i, j -1), (i, j+1)])
            return res

        def isConnected(i, j):
            return i == 0 or any([0 <= x < m and 0 <=y < n and grid[x][y] == 2 for x, y in [(i-1, j), (i + 1, j), (i, j -1), (i, j+1)]])

        for i, j in hits:
            grid[i][j] -= 1
        for i in range(n):
            dfs(0, i)
        res = [0] * len(hits)
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j] == 1 and isConnected(i, j):
                res[k] = dfs(i, j) - 1
        return res
# @lc code=end

