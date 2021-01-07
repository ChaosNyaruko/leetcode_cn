#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n  = len(isConnected)
        visited = set()
        res = 0
        def helper(x):
            for i in range(n):
                if i not in visited and isConnected[i][x] == 1:
                    visited.add(i)
                    helper(i)
        for i in range(n):
            if i not in visited:
                helper(i)
                res += 1
        return res
# @lc code=end

