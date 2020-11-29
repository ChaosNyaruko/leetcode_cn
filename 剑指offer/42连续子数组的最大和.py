class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        dp = nums[0]
        for i in range(1, len(nums)):
            if dp + nums[i] > nums[i]:
                dp = nums[i] + dp
            else:
                dp = nums[i]
            res = max(res, dp)
        return res