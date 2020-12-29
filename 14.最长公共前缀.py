#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, len(strs))):
                return strs[0][:i]
        return strs[0]
# @lc code=end

