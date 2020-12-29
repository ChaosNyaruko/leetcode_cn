#
# @lc app=leetcode.cn id=330 lang=python3
#
# [330] 按要求补齐数组
#

# @lc code=start
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        res = 0
        i = 0
        while miss <= n:
            if  i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                res += 1
                miss += miss
        return res
        # @lc code=end

