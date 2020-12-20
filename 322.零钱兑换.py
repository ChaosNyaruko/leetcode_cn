#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        dp = [sys.maxsize for _ in range(amount + 1)]
        dp[0] = 0
        for num in range(1, amount+1):
            for coin in coins:
                if num - coin >= 0:
                    dp[num] = min(dp[num], dp[num - coin] + 1)
        return dp[amount] if dp[amount] < sys.maxsize else -1
# @lc code=end

