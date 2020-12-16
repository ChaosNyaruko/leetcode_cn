#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # chs = pattern.split()
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        chDict = dict()
        wordDict = dict()
        for ch, word in zip(pattern, words):
            if (ch in chDict and chDict[ch] != word) or (word in wordDict and wordDict[word] != ch):
                return False
            chDict[ch] = word
            wordDict[word] = ch
        return True


# @lc code=end

