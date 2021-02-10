#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (38.45%)
# Likes:    242
# Dislikes: 0
# Total Accepted:    56.2K
# Total Submissions: 144.2K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
#
# 示例1:
#
#
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#
#
#
#
# 示例2:
#
#
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#
#
#
#
# 注意：
#
#
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
#
#
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        cnt = [0] * 26
        for c in s1:
            cnt[ord(c) - ord('a')] -= 1

        left, right = 0, 0
        while right < n:
            cnt[ord(s2[right]) - ord('a')] += 1
            while cnt[ord(s2[right]) - ord('a')] > 0:
                cnt[ord(s2[left]) - ord('a')] -= 1
                left += 1
            if right - left + 1 == m:
                return True
            right += 1

        return False
# @lc code=end

