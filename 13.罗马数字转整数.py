#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dic = collections.defaultdict(int)
        dic["I"] = 1
        dic["V"] = 5
        dic["X"] = 10
        dic["L"] = 50
        dic["C"] = 100
        dic["D"] = 500
        dic["M"] = 1000
        pre = dic[s[0]]
        sum = 0
        for i in range(1, len(s)):
            cur = dic[s[i]]
            if cur > pre:
                sum -= pre
            else:
                sum += pre
            pre = cur
        sum += pre
        return sum
            

# @lc code=end

