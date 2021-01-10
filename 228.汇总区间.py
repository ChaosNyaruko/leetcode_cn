#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        i = 0
        res = []
        while i < n:
            low = i
            i += 1
            while i < n and nums[i] == nums[i - 1] + 1:
                i += 1
            high = i - 1
            if low < high:
                res.append(str(nums[low]) + "->" + str(nums[high]))
            elif low == high:
                res.append(str(nums[low]))

        return res
# @lc code=end

