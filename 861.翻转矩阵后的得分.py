#
# @lc app=leetcode.cn id=861 lang=python3
#
# [861] 翻转矩阵后的得分
#

# @lc code=start
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])

        res = m * (1 << (n - 1))
        for j in range(1, n):
            nOnes = 0
            for i in range(m):
                if A[i][0] == 1:
                    nOnes += A[i][j]
                else:
                    nOnes += 1 - A[i][j]
            k = max(nOnes, m - nOnes)
            res += k * (1 << (n - j - 1))

        return res

        
# @lc code=end

