#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        # reverse(0, n - k - 1)
        # reverse(n - k, n - 1)
        # reverse(0, len(nums) - 1)
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
            
            
# @lc code=end

