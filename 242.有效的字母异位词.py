#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        for c in t:
            index = ord(c) - ord('a')
            if cnt[index] == 0:
                return False
            cnt[index] -= 1
        return True
# @lc code=end

