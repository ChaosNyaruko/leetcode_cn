#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
# https://leetcode-cn.com/problems/burst-balloons/description/
#
# algorithms
# Hard (67.32%)
# Likes:    600
# Dislikes: 0
# Total Accepted:    35.1K
# Total Submissions: 52.2K
# Testcase Example:  '[3,1,5,8]'
#
# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
# 
# 现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的
# left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
# 
# 求所能获得硬币的最大数量。
# 
# 说明:
# 
# 
# 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 
# 
# 示例:
# 
# 输入: [3,1,5,8]
# 输出: 167 
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
# 
# 
#

# @lc code=start
class Solution:
    def maxCoins_DFS(self, nums: List[int]) -> int:
        val = [1] + nums + [1]
        n = len(val)
        memo = [[-1 for _ in range(n)] for _ in range(n)]
        # memo[i][j]: (i, j) max coins
        def helper(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            if i >= j - 1:
                memo[i][j] = 0
                return 0
            cur = -1
            for mid in range(i + 1, j):
                tmp = val[i] * val[j] * val[mid] + helper(i, mid) + helper(mid, j)
                cur = max(cur, tmp)

            memo[i][j] = cur
            return cur
        return helper(0, n-1)

        
    def maxCoins(self, nums: List[int]) -> int:
        val = [1] + nums + [1]
        n = len(val)
        memo = [[0 for _ in range(n)] for _ in range(n)]
        for l in range(1, n - 1):
            for i in range(0, n - l - 1):
                j = i + l + 1
                for mid in range(i + 1, j):
                    # print("i=%d, len=%d, j=%d, mid=%d" % (i, l, j, mid))
                    memo[i][j] = max(memo[i][j], val[mid] * val[i] * val[j] + memo[i][mid] + memo[mid][j])
        
        return memo[0][n -1]

# @lc code=end

