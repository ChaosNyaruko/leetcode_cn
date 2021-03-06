#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (40.68%)
# Likes:    858
# Dislikes: 0
# Total Accepted:    106.8K
# Total Submissions: 262.6K
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 
# 
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        mx, mn, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            preMx, preMn = mx, mn
            mx = max(nums[i], preMx * nums[i], preMn * nums[i])
            mn = min(nums[i], preMx * nums[i], preMn * nums[i])
            res = max(res, mx)
        return res
# @lc code=end

