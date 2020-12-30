#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Of course we have efficient algorithms such KMP、Rabin-Karp、Boyer-Moore...
        # We solve it in the most direct way: brute force
        # The difficulty is how to write it elegant, considering all corner cases

        i = 0
        while True:
            j = 0
            while True:
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return -1
                if needle[j] != haystack[i+j]:
                    break
                j += 1
            i += 1
        
# @lc code=end

