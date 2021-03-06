#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (57.26%)
# Likes:    637
# Dislikes: 0
# Total Accepted:    67.2K
# Total Submissions: 117.4K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
# 
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 
# 
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 
# 
# 示例:
# 
# 输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 
#

# @lc code=start
class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        # not consider space optimization for comprehension
        hasStock = [0] * len(prices)
        noStockInCoolDown = [0] * len(prices)
        noStockOutCoolDown = [0] * len(prices)
        hasStock[0] = -prices[0]
        for i in range(1, len(prices)):
            hasStock[i] = max(hasStock[i - 1], noStockOutCoolDown[i - 1] - prices[i])
            noStockInCoolDown[i] = hasStock[i - 1] + prices[i]
            noStockOutCoolDown[i] = max(noStockInCoolDown[i - 1], noStockOutCoolDown[i - 1]) 
        
        return max(noStockOutCoolDown[len(prices) - 1], noStockInCoolDown[len(prices) - 1])

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        # space optimization 
        noStockInCoolDown = 0
        noStockOutCoolDown = 0
        hasStock = -prices[0]
        for i in range(1, len(prices)):
            hasStock = max(hasStock, noStockOutCoolDown - prices[i])
            noStockOutCoolDown = max(noStockInCoolDown, noStockOutCoolDown) 
            noStockInCoolDown = hasStock + prices[i]
        
        return max(noStockOutCoolDown, noStockInCoolDown)

# @lc code=end

