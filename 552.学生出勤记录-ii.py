class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000000 + 7
        dp = [[[0, 0, 0], [0, 0, 0]]for _ in range(n + 1)]

        dp[0][0][0] = 1
        for i in range(1, n + 1):
            # P 结尾
            for j in range(2):
                for k in range(3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD

            # A 结尾
            for k in range(3):
                dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % MOD

            # L 结尾
            for j in range(2):
                for k in range(1, 3):
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % MOD

        res = 0
        for j in range(2):
            for k in range(3):
                res = (res + dp[n][j][k]) % MOD

        return res


