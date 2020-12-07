#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive_set(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in num_set:
            if num - 1 not in num_set:
                cur = num
                cur_length = 1
                while cur + 1 in num_set:
                    cur += 1
                    cur_length += 1
                res = max(res, cur_length)
        return res
    def longestConsecutive(self, nums: List[int]) -> int:
        m = dict()
        res = 0
        for num in nums:
            if num in m:
                continue
            left = 0
            if num - 1 in m:
                left = m[num - 1] 
            right = 0
            if num + 1 in m:
                right = m[num + 1]
            cur = left + right + 1
            res = max(res, cur)
            m[num - left] = cur 
            m[num + right] = cur 
            m[num] = cur
        return res
# @lc code=end

