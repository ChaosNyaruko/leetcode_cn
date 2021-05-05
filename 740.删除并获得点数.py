class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def rob(array):
            x_1 = array[0]
            x = max(array[0], array[1])
            for i in range(2, len(array)):
                x_1, x = x, max(x_1 + array[i], x)
            return x

        maxVal = max(nums)
        total = [0] * (maxVal + 1)
        for val in nums:
            total[val] += val

        return rob(total)

