class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # P + N = S P - N = target
        S = sum(nums)
        if (S + target) % 2 == 1 or target > S:
            return 0
        s = (S + target) // 2
        dp = [[0 for _ in range(0, s + 1)] for _ in range(0, len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for k in range(0, s + 1):
                dp[i][k] = dp[i - 1][k]
                if nums[i - 1] <= k:
                    dp[i][k] += dp[i - 1][k - nums[i - 1]]
        return dp[len(nums)][s]
