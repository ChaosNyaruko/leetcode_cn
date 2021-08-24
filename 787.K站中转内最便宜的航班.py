class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [[float('inf')] * n for _ in range(k + 2)]
        dp[0][src] = 0
        for i in range(1, k + 2):
            for s, d, price in flights:
                dp[i][d] = min(dp[i][d], dp[i - 1][s] + price)

        ans = float('inf')
        for i in range(1, k + 2):
            ans = min(ans, dp[i][dst])

        return ans if ans != float('inf') else -1
