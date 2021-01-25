#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
# https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (46.35%)
# Likes:    414
# Dislikes: 0
# Total Accepted:    40.1K
# Total Submissions: 86.6K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# 给定一个整数矩阵，找出最长递增路径的长度。
# 
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
# 
# 示例 1:
# 
# 输入: nums = 
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径为 [1, 2, 6, 9]。
# 
# 示例 2:
# 
# 输入: nums = 
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
# 
# 
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        def helper(i, j):
            if memo[i][j] != -1:
                return memo[i][j] 
            res = 1           
            for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = i + direction[0], j + direction[1]
                if nx < 0 or nx >= m or ny < 0 or ny >=n or matrix[nx][ny] <= matrix[i][j]:
                    continue
                res = max(res, 1 + helper(nx, ny))

            memo[i][j] = res
            return memo[i][j]


        res = 1
        for i in range(m):
            for j in range(n):
                tmp = helper(i, j)
                res = max(res, tmp)
        
        return res

# @lc code=end

class Solution {
    int m, n;
    vector<vector<int>> memo;
    int dir[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int helper(vector<vector<int>> &matrix, int x, int y){
        if(memo[x][y] != 0){
            return memo[x][y];
        }
        int res = 1;
        for(int i = 0; i<4; i++){
            int nx = x + dir[i][0], ny = y + dir[i][1];
            if(nx >= m || nx <0 || ny >= n || ny < 0 || matrix[nx][ny] <= matrix[x][y])
                continue;
            int len = 1 + helper(matrix, nx, ny);
            res = max(res, len);
        }
        memo[x][y] = res;
        return res;
    }
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m = matrix.size();
        if(m == 0) return 0;
        n = matrix[0].size();
        memo = vector<vector<int>>(m, vector<int>(n, 0));
        int res = 1;
        for(int i = 0; i<m; i++){
            for(int j = 0; j<n; j++){
                int tmp = helper(matrix, i, j);
                res = max(res, tmp);
            }
        }
        return res;
    }
};