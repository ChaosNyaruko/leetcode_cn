#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        majority = -1
        for num in nums:
            if cnt == 0:
                cnt += 1
                majority = num
            else:
                if majority == num:
                    cnt += 1
                else:
                    cnt -= 1
        return majority

# @lc code=end

