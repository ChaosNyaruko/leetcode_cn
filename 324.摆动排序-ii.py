from typing import List
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#
# https://leetcode-cn.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (36.68%)
# Likes:    226
# Dislikes: 0
# Total Accepted:    17.8K
# Total Submissions: 48.4K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# 给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
# 
# 你可以假设所有输入数组都可以得到满足题目要求的结果。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,5,1,1,6,4]
# 输出：[1,6,1,5,1,4]
# 解释：[1,4,1,5,1,6] 同样是符合题目要求的结果，可以被判题程序接受。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,3,2,2,3,1]
# 输出：[2,3,1,3,1,2]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 题目数据保证，对于给定的输入 nums ，总能产生满足题目要求的结果
# 
# 
# 
# 
# 进阶：你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？
# 
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        def quickSelect(nums, begin, end, n):
            # 快速排序中的一次划分
            def partition(begin,end):
                left,right = begin,end
                while left < right:
                    while left < right and nums[left] < nums[right]:right -= 1
                    if left < right:
                        nums[left],nums[right] = nums[right],nums[left]
                        left += 1
                    while left < right and nums[left] < nums[right]: left += 1
                    if left < right:
                        nums[left],nums[right] = nums[right],nums[left]
                        right -= 1
                return left

            # 找到中位数对应的数值
            left,right = begin, end-1
            while True:
                pivot = partition(left,right)
                if pivot == mid:break
                elif pivot > mid:right = pivot - 1
                else:left = pivot + 1

        def quickSelect1(nums, begin, end, n):
            t = nums[end - 1]
            i, j = begin, begin
            while j < end:
                if nums[j] <= t:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                else:
                    j += 1
                
            if i - 1 > n:
                quickSelect(nums, begin, i - 1, n)
            elif i <= n:
                quickSelect(nums, i, end, n)
        mid = (len(nums) - 1) // 2
        quickSelect(nums, 0, len(nums), -1)
        # mid = nums[len(nums) // 2]
        midNum = nums[mid]
        # 3-way partition
        i, j, k = 0, 0, len(nums) - 1
        while j < k:
            if nums[j] > midNum:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            elif nums[j] < midNum:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1
            
        tmp1 = nums[:mid + 1]
        tmp2 = nums[mid + 1:]
        # print(tmp1)
        # print(tmp2)
        for i in range(len(tmp1)):
            nums[2 * i] = tmp1[len(tmp1) - 1 - i]
        for i in range(len(tmp2)):
            nums[2 * i + 1] = tmp2[len(tmp2) - 1 - i]


# @lc code=end


def quickSelect(nums, begin, end, n):
            # 快速排序中的一次划分
        def partition(begin,end):
            left,right = begin,end
            while left < right:
                while left < right and nums[left] < nums[right]:right -= 1
                if left < right:
                    nums[left],nums[right] = nums[right],nums[left]
                    left += 1
                while left < right and nums[left] < nums[right]: left += 1
                if left < right:
                    nums[left],nums[right] = nums[right],nums[left]
                    right -= 1
            return left

        # 找到中位数对应的数值
        left,right = begin, end-1
        while True:
            pivot = partition(left,right)
            if pivot == mid:break
            elif pivot > mid:right = pivot - 1
            else:left = pivot + 1

nums = [5,4,3,2,1, 8, 20, 2]
mid = (len(nums) - 1) // 2
quickSelect(nums, 0, len(nums), -1)
print(nums)