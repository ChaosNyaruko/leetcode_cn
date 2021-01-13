#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        print(bin(n & 0xffffffff))
        n = (n >> 16) | (n << 16)
        print(bin(n & 0xffffffff))
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        print(bin(n & 0xffffffff))
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        print(bin(n & 0xffffffff))
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        print(bin(n & 0xffffffff))
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        print(bin(n & 0xffffffff))
        return n
        
# @lc code=end

sl = Solution()
sl.reverseBits(4294967293)