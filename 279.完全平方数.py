#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] denotes the minimum number of square numbers composing i
        # what we want is dp[n]
        dp = [0] * (n + 1)
        if n == 1:
            return 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = i
            for j in range(1, i):
                if i < j * j:
                    break
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]
# @lc code=end

