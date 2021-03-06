#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#
# https://leetcode-cn.com/problems/power-of-three/description/
#
# algorithms
# Easy (47.90%)
# Likes:    136
# Dislikes: 0
# Total Accepted:    68.6K
# Total Submissions: 143.1K
# Testcase Example:  '27'
#
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。
# 
# 整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3^x
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 27
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：n = 0
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：n = 9
# 输出：true
# 
# 
# 示例 4：
# 
# 
# 输入：n = 45
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 
# 
# 
# 
# 
# 进阶：
# 
# 
# 你能不使用循环或者递归来完成本题吗？
# 
# 
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        return n > 0 and (n % 3 == 0) and self.isPowerOfThree(n // 3) 
# @lc code=end

