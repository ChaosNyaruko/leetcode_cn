#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#
# https://leetcode-cn.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (55.25%)
# Likes:    224
# Dislikes: 0
# Total Accepted:    32.8K
# Total Submissions: 58.1K
# Testcase Example:  '[1,2,2,3,1]'
#
# 给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
#
# 你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
#
#
#
# 示例 1：
#
#
# 输入：[1, 2, 2, 3, 1]
# 输出：2
# 解释：
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
#
#
# 示例 2：
#
#
# 输入：[1,2,2,3,1,4,2]
# 输出：6
#
#
#
#
# 提示：
#
#
# nums.length 在1到 50,000 区间范围内。
# nums[i] 是一个在 0 到 49,999 范围内的整数。
#
#
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mp = dict()
        for i, num in enumerate(nums):
            if num in mp:
                mp[num][0] += 1
                mp[num][2] = i
            else:
                mp[num] = [1, i, i]

        minLen, maxCnt = 0, 0
        for num in nums:
            count, left, right = mp[num][0], mp[num][1], mp[num][2]
            if count > maxCnt:
                maxCnt = count
                minLen = right - left + 1
            elif count == maxCnt:
                minLen = min(minLen, right - left + 1)

        return minLen

# @lc code=end

