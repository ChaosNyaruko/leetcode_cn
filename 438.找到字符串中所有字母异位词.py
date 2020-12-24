#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = [0] * 128
        for ch in p:
           cnt[ord(ch)] += 1
        left = right = 0
        count = len(p)
        res = []
        while right < len(s):
            if cnt[ord(s[right])] > 0:
                count -= 1
            cnt[ord(s[right])] -= 1
            while count == 0:
                if right - left + 1 == len(p):
                    res.append(left)
                cnt[ord(s[left])] += 1
                if cnt[ord(s[left])] > 0:
                    count += 1
                left += 1
            right += 1
        return res

# @lc code=end

