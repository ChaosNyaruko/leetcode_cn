#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# https://leetcode-cn.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (40.32%)
# Likes:    128
# Dislikes: 0
# Total Accepted:    24.5K
# Total Submissions: 60.8K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
# 
# 
# 
# 示例：
# 
# 
# 输入：[1,12,-5,-6,50,3], k = 4
# 输出：12.75
# 解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 
# 
# 提示：
# 
# 
# 1 k n 
# 所给数据范围 [-10,000，10,000]。
# 
# 
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        m = total

        for i in range(k, len(nums)):
            total = total - nums[i - k] + nums[i]
            m = max(m, total)

        return m / k

        
# @lc code=end

