#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        sign = '+'
        num = 0
        stk = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + (ord(s[i]) - ord('0'))
            if not s[i].isdigit() and s[i] != ' ' or i == len(s) - 1:
                if sign == '-':
                    stk.append(-num)
                elif sign == '+':
                    stk.append(num)
                elif sign == '*':
                    stk.append(stk.pop() * num)
                elif sign == '/':
                    last = stk.pop()
                    if last < 0:
                        new =  - (-last // num)
                    else:
                        new = last // num
                    stk.append(new)
                sign = s[i]
                num = 0
        return sum(stk)
                
            
# @lc code=end

sl = Solution()
print(sl.calculate("14-3/2"))