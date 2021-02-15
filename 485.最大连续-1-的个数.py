#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#
# https://leetcode-cn.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (57.07%)
# Likes:    171
# Dislikes: 0
# Total Accepted:    73.8K
# Total Submissions: 127.7K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# 给定一个二进制数组， 计算其中最大连续1的个数。
# 
# 示例 1:
# 
# 
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 
# 
# 注意：
# 
# 
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。
# 
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes_my(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while l < len(nums):
            if nums[l] == 1:
                r = l
                while r < len(nums) and nums[r] == 1:
                    r += 1
                res = max(r - l, res)
            l = max(l + 1, r)
        return res
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0
        res = max(res, count)
        return res
# @lc code=end

