#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        dx, dy = coordinates[0][0], coordinates[0][1]
        n = len(coordinates)
        for i in range(n):
            coordinates[i][0] -= dx
            coordinates[i][1] -= dy
            A, B = coordinates[1][1], -coordinates[1][0]
        for i in range(2, n):
            x, y = coordinates[i][0], coordinates[i][1]
            if A * x + B * y != 0:
                return False
        return True
# @lc code=end

