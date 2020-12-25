#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        res = 0
        while xor:
            res += 1
            xor = xor & (xor - 1)
        return res
# @lc code=end

