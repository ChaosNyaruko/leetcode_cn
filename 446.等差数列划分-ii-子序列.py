class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        f = [defaultdict(int) for _ in nums]

        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                cnt = f[j][d]
                f[i][d] += cnt + 1
                res += cnt

        return res
