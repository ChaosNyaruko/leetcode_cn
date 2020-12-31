#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False for _ in range(10)] for _ in range(9)]
        cols = [[False for _ in range(10)] for _ in range(9)]
        boxes = [[False for _ in range(10)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                boxIndex = i // 3 * 3 + j //3
                if rows[i][num] or cols[j][num] or boxes[boxIndex][num]:
                    return False
                rows[i][num] = True
                cols[j][num] = True
                boxes[boxIndex][num] = True
        return True 
        
# @lc code=end

