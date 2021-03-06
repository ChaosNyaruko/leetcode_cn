#
# @lc app=leetcode.cn id=1438 lang=python3
#
# [1438] 绝对差不超过限制的最长连续子数组
#
# https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
#
# algorithms
# Medium (40.73%)
# Likes:    94
# Dislikes: 0
# Total Accepted:    9.4K
# Total Submissions: 23.1K
# Testcase Example:  '[8,2,4,7]\n4'
#
# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于
# limit 。
# 
# 如果不存在满足条件的子数组，则返回 0 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [8,2,4,7], limit = 4
# 输出：2 
# 解释：所有子数组如下：
# [8] 最大绝对差 |8-8| = 0 <= 4.
# [8,2] 最大绝对差 |8-2| = 6 > 4. 
# [8,2,4] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
# [2] 最大绝对差 |2-2| = 0 <= 4.
# [2,4] 最大绝对差 |2-4| = 2 <= 4.
# [2,4,7] 最大绝对差 |2-7| = 5 > 4.
# [4] 最大绝对差 |4-4| = 0 <= 4.
# [4,7] 最大绝对差 |4-7| = 3 <= 4.
# [7] 最大绝对差 |7-7| = 0 <= 4. 
# 因此，满足题意的最长子数组的长度为 2 。
# 
# 
# 示例 2：
# 
# 输入：nums = [10,1,2,4,7,2], limit = 5
# 输出：4 
# 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
# 
# 
# 示例 3：
# 
# 输入：nums = [4,2,2,2,4,4,2,2], limit = 0
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left, right = 0, 0
        res = 0
        # 用非递增栈维护窗口最大值
        # 用非递减栈维护窗口最小值
        queMax, queMin = deque(), deque()
        while right < len(nums):
            while queMax and nums[right] > queMax[-1]:
                queMax.pop()
            while queMin and nums[right] < queMin[-1]:
                queMin.pop()

            queMin.append(nums[right])
            queMax.append(nums[right])

            while queMin and queMax and (queMax[0] - queMin[0] > limit):
                if nums[left] == queMax[0]:
                    queMax.popleft()
                if nums[left] == queMin[0]:
                    queMin.popleft()
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res

# @lc code=end

