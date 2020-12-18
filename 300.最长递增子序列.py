#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # normal n^2
        # dp[i] max inscreasing sequence ending at nums[i]
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        res = dp[0]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res
# @lc code=end

