#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if i >= 2:
                a,b = int(s[i-2]), int(s[i-1])
                c = 10 * a + b
                if c >=10 and c <= 26:
                    dp[i] += dp[i-2]
            cur = int(s[i - 1])
            if cur >= 1 and cur <= 9:
                dp[i] += dp[i - 1]
            # print("dp[%d]=%d"%(i, dp[i]))
        return dp[len(s)]

# @lc code=end

