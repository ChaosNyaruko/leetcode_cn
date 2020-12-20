#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1
        inStack = [False] * 26
        res = []
        for ch in s:
            if not inStack[ord(ch) - ord("a")]:
               while len(res) != 0 and res[-1] > ch:
                   # this can be remove cuz there still remains stack.back
                   if cnt[ord(res[-1]) - ord("a")] > 0:
                       inStack[ord(res[-1]) - ord("a")] = False 
                       res.pop()
                   else:
                        break
               res.append(ch)
            inStack[ord(ch) - ord("a")] = True
            cnt[ord(ch) - ord("a")] -= 1
        
        return "".join(res)
# @lc code=end

