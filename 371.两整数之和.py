#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#
# https://leetcode-cn.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (57.17%)
# Likes:    355
# Dislikes: 0
# Total Accepted:    44K
# Total Submissions: 76.9K
# Testcase Example:  '1\n2'
#
# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
# 
# 示例 1:
# 
# 输入: a = 1, b = 2
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: a = -2, b = 3
# 输出: 1
# 
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0x100000000
        INT_MAX = 0x7fffffff
        INT_MIN = INT_MAX + 1
        while b:
            carry = (a & b) << 1
            a = (a ^ b) % mask
            b = carry % mask
        return a if a <= INT_MAX else ~(a ^ 0xffffffff)
        
# @lc code=end

