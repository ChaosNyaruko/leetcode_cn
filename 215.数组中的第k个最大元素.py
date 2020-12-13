#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.53%)
# Likes:    824
# Dislikes: 0
# Total Accepted:    232.5K
# Total Submissions: 360.3K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 示例 1:
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 说明: 
# 
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# 
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums: List[int], l, r) -> int:
            i, j = l + 1, r
            pivot = nums[l]
            while i <= j:
                while i < j and nums[i] >= pivot: i += 1
                while j >= i and nums[j] <= pivot: j -= 1
                if i >= j: break
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            # 要让pivot左边是大的，右边是小的，nums[l]必须和大的交换
            # 所以对j要多移动一格
            nums[l], nums[j] = nums[j], nums[l]
            return j
        
        random.shuffle(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            p = partition(nums, l, r)
            if p == k - 1:
                return nums[p]
            elif p > k -1:
                r = p - 1
            else:
                l = p + 1
        return nums[k - 1]


# @lc code=end

