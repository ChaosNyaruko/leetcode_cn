#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        # print(res)
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = r * res[i]
            r *= nums[i]
        return res
# @lc code=end

