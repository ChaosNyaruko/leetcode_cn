#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS_1(self, nums: List[int]) -> int:
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

    def lengthOfLIS(self, nums: List[int]) -> int:
        # nlog(n)
        # tails[i] means the minimum ending element among all LISs at length i+1
        if len(nums) == 0:
            return 0
        tails = [nums[0]]
        for i in range(1, len(nums)):
            # find the smallest element bigger than (or equal to)nums[i] and replace it
            # if nums[i] is smaller than (or equal to) all tails[i], tails[1]
            if nums[i] > tails[-1]:
                tails.append(nums[i])
            else:
                l, r = 0, len(tails) - 1
                while l < r:
                    m = l + (r - l) // 2
                    if tails[m] < nums[i]:
                        l = m + 1
                    else:
                        r = m
                # print("tails", tails, "tails[l]", tails[l], "nums[i]", nums[i])
                tails[l] = nums[i]
        return len(tails)
        # 爱你~
# @lc code=end

