#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(0, numRows):
            row = []
            for j in range(0, i+1):
                if j == i or j == 0:
                    row.append(1)
                else:
                    row.append(ret[i-1][j] + ret[i-1][j - 1])
            ret.append(row)
        
        return ret
# @lc code=end

