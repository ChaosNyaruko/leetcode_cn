#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ret = 0
        for ch in s:
            ret ^= ord(ch)
        for ch in t:
            ret ^= ord(ch)
        return chr(ret)
# @lc code=end

