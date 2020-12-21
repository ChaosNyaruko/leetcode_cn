#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + int(i & 1) # Attention! or dp[i] will be one bit
            # dp[i] = dp[i // 2] + i % 2
            print("i=%d i>>1=%d i&1=%d, dp[i]=%d, dp[i>>1]=%d"%(i, i>>1, i&1, dp[i], dp[i>>1]))
            
        return dp
        
    def countBits_1(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp
# @lc code=end

