#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#
# https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (42.07%)
# Likes:    518
# Dislikes: 0
# Total Accepted:    40.1K
# Total Submissions: 95.3K
# Testcase Example:  '[5,2,6,1]'
#
# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
# nums[i] 的元素的数量。
# 
# 
# 
# 示例：
# 
# 输入：nums = [5,2,6,1]
# 输出：[2,1,1,0] 
# 解释：
# 5 的右侧有 2 个更小的元素 (2 和 1)
# 2 的右侧仅有 1 个更小的元素 (1)
# 6 的右侧有 1 个更小的元素 (1)
# 1 的右侧有 0 个更小的元素
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(l, r):
            # print("mergeSort", l, r)
            if l >= r:
                return
            mid = l + (r - l) // 2
            mergeSort(l, mid)
            mergeSort(mid + 1, r)
            merge(l, r)

        def merge(l, r):
            # print("merge", l, r)
            if l >= r:
                return
            mid = l + (r - l) // 2
            l1, l2 = l, mid + 1
            p = 0
            tmp = [0] * (r - l + 1)
            rightcnt = 0
            while l1 <= mid and l2 <= r:
                if nums[index[l1]] > nums[index[l2]]:
                    rightcnt += 1
                    tmp[p] = index[l2]
                    l2 += 1
                    p += 1
                else:
                    count[index[l1]] += rightcnt
                    tmp[p] = index[l1]
                    l1 += 1
                    p += 1
            while l1 <= mid:
                count[index[l1]] += rightcnt
                tmp[p] = index[l1]
                l1 += 1
                p += 1
            while l2 <= r:
                tmp[p] = index[l2]
                l2 += 1
                p += 1
            for i in range(r - l + 1):
                index[i + l] = tmp[i]
            return

        count = [0] * len(nums)
        # i -> index[i]: i在处理中的某个排好序的数组的索引, index[i]为在原nums中的索引
        index = list(range(len(nums)))
        mergeSort(0, len(nums) - 1)
        return count
# @lc code=end

