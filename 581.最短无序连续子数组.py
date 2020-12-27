#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Medium (35.54%)
# Likes:    459
# Dislikes: 0
# Total Accepted:    45K
# Total Submissions: 126.6K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 
# 你找到的子数组应是最短的，请输出它的长度。
# 
# 示例 1:
# 
# 
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
# 
# 
# 说明 :
# 
# 
# 输入的数组长度范围在 [1, 10,000]。
# 输入的数组可能包含重复元素 ，所以升序的意思是<=。
# 
# 
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        right, left = -2, -1
        mx = -sys.maxsize - 1 #float("-inf")
        mn = sys.maxsize
        for i in range(len(nums)):
            mx = max(mx, nums[i])
            if nums[i] < mx:
                right = i
        
            mn = min(mn, nums[len(nums) - 1 - i])
            if nums[len(nums) - 1 - i] > mn:
                left = len(nums) - 1 - i
        
        return right - left + 1
# @lc code=end

