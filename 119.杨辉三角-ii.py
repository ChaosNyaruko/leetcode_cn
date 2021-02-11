#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (62.69%)
# Likes:    224
# Dislikes: 0
# Total Accepted:    86.8K
# Total Submissions: 138.2K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 3
# 输出: [1,3,3,1]
# 
# 
# 进阶：
# 
# 你可以优化你的算法到 O(k) 空间复杂度吗？
# 
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1)
        row[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        return row
# @lc code=end

