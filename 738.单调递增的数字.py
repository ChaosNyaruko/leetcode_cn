#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        strNN = str(N)
        strN = list(strNN) 
        n = len(strN)
        i = 1
        while i < n and strN[i-1] <= strN[i]:
            i += 1
        if i < n:
            while i > 0 and strN[i-1] > strN[i]:
                strN[i - 1] = chr(ord(strN[i - 1]) - 1) 
                i -= 1
            i += 1
            while i < n:
                strN[i] = "9"
                i += 1
        # print(strN)
        return int("".join(strN)) 


# @lc code=end
