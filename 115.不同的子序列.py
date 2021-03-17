class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        # dp[i][j] the result of s[0:i] and t[0:j]
        # and the answer will be dp[m][n]
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # boundaries
        for i in range(m + 1):
            dp[i][0] = 1
        for j in range(1, n + 1):
            dp[0][j] = 0

        for j in range(n):
            for i in range(m):
                if s[i] == t[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i][j + 1]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
        return dp[m][n]

