#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (50.16%)
# Likes:    734
# Dislikes: 0
# Total Accepted:    55.6K
# Total Submissions: 110.9K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = []
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [["0"]]
# 输出：0
# 
# 
# 示例 4：
# 
# 
# 输入：matrix = [["1"]]
# 输出：1
# 
# 
# 示例 5：
# 
# 
# 输入：matrix = [["0","0"]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# rows == matrix.length
# cols == matrix[0].length
# 0 
# matrix[i][j] 为 '0' 或 '1'
# 
# 
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        left = [0] * n
        right = [n] * n
        height = [0] * n
        res = 0
        for i in range(m):
            curLeft = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(curLeft, left[j])
                else:
                    height[j] = 0
                    left[j] = 0
                    curLeft = j + 1
            
            curRight = n
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(curRight, right[j])
                else:
                    right[j] = n
                    curRight = j
            
            for j in range(n):
                res = max(res, height[j]*(right[j] - left[j]))
        return res
                

# @lc code=end

