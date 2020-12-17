#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        nonzeros = 0
        while cur < len(nums):
            if nums[cur] != 0:
                # reduce swap times
                if cur != nonzeros:
                    nums[nonzeros], nums[cur] = nums[cur], nums[nonzeros]
                nonzeros += 1
        
            cur += 1
# @lc code=end

