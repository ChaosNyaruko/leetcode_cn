#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode-cn.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (65.57%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    54.4K
# Total Submissions: 83K
# Testcase Example:  '1'
#
# 写一个程序，输出从 1 到 n 数字的字符串表示。
# 
# 1. 如果 n 是3的倍数，输出“Fizz”；
# 
# 2. 如果 n 是5的倍数，输出“Buzz”；
# 
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
# 
# 示例：
# 
# n = 15,
# 
# 返回:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
# 
# 
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for num in range(1, n + 1):
            divisibleBy3 = (num % 3 == 0)
            divisibleBy5 = (num % 5 == 0)
            if divisibleBy3 and divisibleBy5:
                res.append("FizzBuzz")
            elif divisibleBy3:
                res.append("Fizz")
            elif divisibleBy5:
                res.append("Buzz")
            else:
                res.append(str(num))
        return res
        
# @lc code=end

