#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = set(wordDict)
        # dp[i] 表示前i个字符（以i-1）为结尾的字符串能不能使用字典里的单词拼成
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                dp[i] = dp[j] and s[j:i] in dic
                if dp[i]:
                    break
        return dp[len(s)]
        
# @lc code=end

