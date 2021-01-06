#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return 
        n = len(board[0])
        if n == 0:
            return
        def helper(x, y):
            if x < 0 or x >= m or y < 0 or y >=n or board[x][y] != 'O':
                return
            board[x][y] = '-'
            helper(x - 1, y)
            helper(x + 1, y)
            helper(x, y + 1)
            helper(x, y - 1)
       
        for j in range(n):
            if board[0][j] == 'O':
                helper(0, j)
            if board[m - 1][j] == 'O':
                helper(m - 1, j)
        
        for i in range(m):
            if board[i][0] == 'O':
                helper(i, 0)
            if board[i][n-1] == 'O':
                helper(i, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '-':
                    board[i][j] = 'O'
        return
# @lc code=end

