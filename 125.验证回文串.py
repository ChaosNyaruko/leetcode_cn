#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():i += 1
            while j > i  and not s[j].isalnum(): j -= 1
            if i == j:
                break
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
# @lc code=end

