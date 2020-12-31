#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(2 ** 31) and divisor == -1:
            return 2 ** 31 - 1
        sign = 1
        dvd = abs(dividend)
        dvs = abs(divisor)
        if (dividend > 0) ^ (divisor > 0):
            sign = -1
        ans = 0
        while dvd >= dvs:
            tmp = dvs
            shift = 1
            while dvd >= (tmp << 1):
                tmp <<= 1
                shift <<= 1
            dvd -= tmp
            ans += shift
        return sign * ans
# @lc code=end

