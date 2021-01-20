#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1, min2 = 1001, 1001
        max1, max2, max3 = -1001, -1001, -1001
        for n in nums:
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n

            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n
        
        return max(min1 * min2 * max1, max1 * max2 * max3)
                
# @lc code=end

