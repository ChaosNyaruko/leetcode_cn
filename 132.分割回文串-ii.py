#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
# https://leetcode-cn.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (44.97%)
# Likes:    272
# Dislikes: 0
# Total Accepted:    22.6K
# Total Submissions: 49.5K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
#
# 返回符合要求的 最少分割次数 。
#
#
#
#
#
# 示例 1：
#
#
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#
#
# 示例 2：
#
#
# 输入：s = "a"
# 输出：0
#
#
# 示例 3：
#
#
# 输入：s = "ab"
# 输出：1
#
#
#
#
# 提示：
#
#
# 1
# s 仅由小写英文字母组成
#
#
#
#
#
import sys
# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        palindrome = [[True for _ in range(n)] for _ in range(n)]
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if i - j == 1:
                    palindrome[i][j] = s[i] == s[j]
                else:
                    palindrome[i][j] = palindrome[i + 1][j - 1] and (s[i] == s[j])


        res = [sys.maxsize] * n
        for i in range(0, n):
            if palindrome[0][i]:
                res[i] = 0
            else:
                for j in range(0, i):
                    if palindrome[j+1][i]:
                        res[i] = min(res[i], res[j] + 1)

        # print(res)
        return res[-1]

# @lc code=end
if __name__ == '__main__':
    sl = Solution()
    s = "leet"
    print(sl.minCut(s))
