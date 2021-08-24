class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        dp = [[float('inf')] * n for _ in range(maxTime + 1)]

        dp[0][0] = passingFees[0]
        for t in range(1, maxTime + 1):
            for i, j, c in edges:
                if c <= t:
                    dp[t][i] = min(dp[t][i], dp[t - c][j] + passingFees[i])
                    dp[t][j] = min(dp[t][j], dp[t - c][i] + passingFees[j])

        ans = min(dp[t][n - 1] for t in range(maxTime + 1))

        return ans if ans != float('inf') else -1
