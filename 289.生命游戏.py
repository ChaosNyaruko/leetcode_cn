#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])
        def liveNeighbours(x, y):
            res = 0
            for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,1),(1,0)]:
                i, j = x+dx, y+dy
                if i >= 0 and i < m and j >= 0  and j < n and abs(board[i][j]) == 1:
                    res += 1 
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    t = liveNeighbours(i, j)
                    if t < 2 or t > 3:
                        board[i][j] = -1
                if board[i][j] == 0:
                    t = liveNeighbours(i, j)
                    if t == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

# @lc code=end

