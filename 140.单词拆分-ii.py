#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dic = set(wordDict)
        memo = dict()
        def helper(s) -> List[str]:
            # print("helper", s)
            if s in memo:
                return memo[s]

            res = []
            if s in dic:
                res.append(s)
            for lastStart in  range(1, len(s)):
                last = s[lastStart:]
                # print("helper", s, "last", last)
                if last in dic:
                    left = s[:lastStart]
                    prev = helper(left)
                    for p in prev:
                        res.append(p + " " + last)


            memo[s] = res
            return res
        return helper(s)
# @lc code=end

