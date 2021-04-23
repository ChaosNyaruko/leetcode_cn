class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        maxSize, maxVal = 1, nums[0]
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > maxSize:
                maxSize = dp[i]
                maxVal = nums[i]
        # print(dp)
        i = n - 1
        res = []
        while i >= 0 and maxSize > 0:
            if dp[i] == maxSize and maxVal % nums[i] == 0:
                res.append(nums[i])
                maxSize -= 1
                maxVal = nums[i]
            i -= 1

        return res

