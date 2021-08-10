class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        res = 0
        l, d = 0, nums[1] - nums[0]
        t = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == d:
                t += 1
            else:
                t = 0
                d = nums[i] - nums[i - 1]
            res += t

        return res

