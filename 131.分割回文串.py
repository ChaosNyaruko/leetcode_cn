#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s: str) -> bool:
            # print("isPalindrome", s)
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True
        res = []
        path = []
        def helper(left):
            # print("path",path,"left", left)
            if left == len(s):
                res.append(path.copy())
                # res.append(path)
                return
            for right in range(left, len(s)):
                # print(s[left:right + 1])
                if isPalindrome(s[left:right + 1]):
                    path.append(s[left:right+1])
                    helper(right + 1)
                    path.pop()
            return
        helper(0)
        return res
# @lc code=end

