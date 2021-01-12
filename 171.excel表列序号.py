#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for c in s:
            x = ord(c) - ord('A') + 1
            res = res * 26 + x
        return res
# @lc code=end

sl = Solution()
res = sl.titleToNumber('ZY')
print(res)