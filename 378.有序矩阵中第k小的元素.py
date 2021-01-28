#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (63.09%)
# Likes:    522
# Dislikes: 0
# Total Accepted:    61.2K
# Total Submissions: 97K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
# 
# 
# 
# 示例：
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# 返回 13。
# 
# 
# 
# 
# 提示：
# 你可以假设 k 的值永远是有效的，1 ≤ k ≤ n^2 。
# 
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def check(mid, k):
            i, j = n - 1, 0 # 左下角
            cnt = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    cnt += i + 1
                    j += 1
                else:
                    i -= 1
            return cnt >= k
        
        l = matrix[0][0]
        r = matrix[n - 1][n - 1]
        while l < r:
            m = l + (r - l) // 2
            if check(m, k):
                r = m
            else:
                l = m + 1

        return l

        
# @lc code=end

