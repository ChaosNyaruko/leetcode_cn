#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def quickSolve(prices):
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        
        n = len(prices)
        if n == 0:
            return 0
        if k >= n/2: return quickSolve(prices)

        # dp[i][j]: at most i transactions, using prices[0...j-1]
        dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
        # print(dp)
        for i in range(1, k + 1):
            tmpMax = -prices[0] # tmpMax: max profix at most k buys and k-1 sells
            for j in range(1, n + 1):
                # print(i, j)
                # tmpMax + prices[j-1]: sells at j-1
                # dp[i][j-1] do nothing at j-1
                dp[i][j] = max(tmpMax + prices[j - 1], dp[i][j-1])
                tmpMax = max(tmpMax, dp[i-1][j-1] - prices[j - 1])
        return dp[k][n]
# @lc code=end

