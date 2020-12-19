#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#
# https://leetcode-cn.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (49.15%)
# Likes:    340
# Dislikes: 0
# Total Accepted:    18K
# Total Submissions: 36.7K
# Testcase Example:  '"()())()"'
#
# 删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
# 
# 说明: 输入可能包含了除 ( 和 ) 以外的字符。
# 
# 示例 1:
# 
# 输入: "()())()"
# 输出: ["()()()", "(())()"]
# 
# 
# 示例 2:
# 
# 输入: "(a)())()"
# 输出: ["(a)()()", "(a())()"]
# 
# 
# 示例 3:
# 
# 输入: ")("
# 输出: [""]
# 
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        def helper(s, last_i, last_j, openp, closep):
            left = 0
            for i in range(last_i, len(s)):
                if s[i] == openp:
                    left += 1
                if s[i] == closep:
                    left -= 1
                if left >= 0:
                    continue
                for j in range(last_j, i + 1):
                    if s[j] == closep and (j == last_j or s[j - 1] != closep):
                        helper(s[0:j] + s[j + 1:], i, j, openp, closep)
                return        
            s = s[::-1]
            if openp == "(":
                helper(s, 0, 0, closep, openp)
            else:
                res.append(s)
                
        helper(s, 0, 0, "(", ")")
        return res
        
# @lc code=end

