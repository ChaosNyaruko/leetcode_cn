class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        l = 0
        operCnt = 0
        res = 1
        for r in range(1, n):
            operCnt += (nums[r] - nums[r - 1]) * (r - l)
            while operCnt > k:
                operCnt -= nums[r] - nums[l]
                l += 1
            res = max(res, r - l + 1)

        return res
