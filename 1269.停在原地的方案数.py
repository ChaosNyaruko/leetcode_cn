class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        maxColumn = min(arrLen - 1, steps)
        dp = [[0 for _ in range(maxColumn + 1)] for _ in range(steps + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7
        # dp[i][j] i步走到位置j的方案数
        for i in range(1, steps + 1):
            for j in range(0, maxColumn + 1):
                dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod
                if j < maxColumn:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod

        return dp[steps][0]
