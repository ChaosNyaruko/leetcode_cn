#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 可被 5 整除的二进制前缀
#

# @lc code=start
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = list()
        prefix = 0
        for a in A:
            prefix = ((prefix << 1) + a)%5
            res.append(prefix == 0)
        return res

        
# @lc code=end

