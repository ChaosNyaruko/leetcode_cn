#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        res = 0
        curMin = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - curMin)
            curMin = min(curMin, prices[i])
        return res
# @lc code=end

