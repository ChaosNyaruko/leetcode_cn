#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h) > 1:
            i1 = -h[0]
            heapq.heappop(h)
            i2 = -h[0]
            heapq.heappop(h)
            x = max(i1, i2) - min(i1, i2)
            heapq.heappush(h, -x)
        return -h[0]
        
# @lc code=end

