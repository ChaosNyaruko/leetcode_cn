#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # without[i] means: max profit without a stock when day-i is over
        # with[i] menas: max profit with a stock when day-i is over
        # Attention: WITH or WITHOUT, not SELLAT or BUYAT
        # suppose fee only needed when selling
        # with[i] = max(with[i - 1], without[i - 1] - price[i]) 
        # without[i] = max(without[i - 1], with[i - 1] + price[i] - fee)
        # without[0] = 0
        # with[0] = -price[0]
        if len(prices) < 2:
            return 0
        dp_without = [0] * len(prices)
        dp_with = [0] * len(prices)
        dp_with[0] = -prices[0]
        dp_without[0] = 0
        for i in range(1, len(prices)):
            dp_with[i] = max(dp_with[i - 1], dp_without[i - 1] - prices[i]) 
            dp_without[i] = max(dp_without[i - 1], dp_with[i - 1] + prices[i] - fee)
        
        return dp_without[len(prices) - 1]

        
# @lc code=end

