#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
# @lc code=end

