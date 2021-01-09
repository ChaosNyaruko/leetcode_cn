#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
# https://leetcode-cn.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (23.48%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    18.8K
# Total Submissions: 80.2K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
# 
# 示例 1:
# 
# 输入: [[1,1],[2,2],[3,3]]
# 输出: 3
# 解释:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# 
# 
# 示例 2:
# 
# 输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出: 4
# 解释:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
# 
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def mygcd(a, b):
            if b == 0:
                return a
            else:
                return mygcd(b, a % b)
        n = len(points)
        res = 0
        for i in range(n):
            freqK = collections.defaultdict(int)
            maxFreqK = 0
            duplicate = 0
            for j in range(i + 1, n):
                dx  = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                   duplicate += 1
                   continue 
                gcd = mygcd(dx, dy)
                # gcd = math.gcd(dx, dy)
                # if dx < 0 and dy > 0:
                #     gcd = -gcd
                p = (dx // gcd, dy//gcd)
                freqK[p] += 1
                maxFreqK = max(maxFreqK, freqK[p])
            # print("base points", points[i], freqK, maxFreqK)
            res = max(res, duplicate + 1 + maxFreqK)
        return res

# @lc code=end

