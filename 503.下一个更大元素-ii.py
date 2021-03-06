#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#
# https://leetcode-cn.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (59.92%)
# Likes:    286
# Dislikes: 0
# Total Accepted:    47.8K
# Total Submissions: 79.7K
# Testcase Example:  '[1,2,1]'
#
# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x
# 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
# 
# 示例 1:
# 
# 
# 输入: [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数； 
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
# 
# 
# 注意: 输入数组的长度不会超过 10000。
# 
#
from typing import List
# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # decreasing(not strictly) stack
        n = len(nums)
        stk = []
        res = [-1] * n
        i = 0
        for i in range(0, n + n):
            i %= n
            # print("i=%d, num=%d" %(i, nums[i]))
            while stk and nums[i] > nums[stk[-1]]:
                res[stk[-1]] = nums[i] 
                stk.pop()
            # print(stk)
            stk.append(i)   
            # print(stk)
        # print("for over", stk)
        
        return res
# @lc code=end
if __name__ == '__main__':
    sl = Solution()
    for m in [[1,2,3,4], 
        [1,2,2,3], 
        [1,2,1],
        [1,1,1,1],
        [1,2,1,1],
        [4,3,2,1]]:
        print(sl.nextGreaterElements(m))
