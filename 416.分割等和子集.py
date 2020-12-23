#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        # print(target)
        dp = [[False] * (target + 1) for _ in range(len(nums))]
        if nums[0] <= target:
            dp[0][nums[0]] = True 
        # print(dp)
        # for i in range(0,len(nums)):
        #     dp[i][0] = True
        for i in range(1, len(nums)):
            for j in range(0, target + 1):
                dp[i][j] = dp[i-1][j] # do not use nums[i]
                if j >= nums[i]:
                    dp[i][j] = dp[i][j] or dp[i-1][j - nums[i]]
        return dp[len(nums) - 1][target]
# @lc code=end

