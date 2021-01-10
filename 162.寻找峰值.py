#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m1 = l + (r - l) // 2
            m2 = m1 + 1
            if nums[m1] < nums[m2]:
                l = m2
            else:
                r = m1
        return l

# @lc code=end

