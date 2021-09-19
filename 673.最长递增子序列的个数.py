class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        cnt = [0] * n
        curMax = 1
        res = 0
        for i in range(n):
            dp[i] = 1
            cnt[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]

            if dp[i] > curMax:
                curMax = dp[i]
                res = cnt[i]
            elif dp[i] == curMax:
                res += cnt[i]
    
        return res
