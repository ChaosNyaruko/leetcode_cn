#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[1])
        end = intervals[0][1]
        ans = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                ans += 1
                end = intervals[i][1]
        return len(intervals) - ans

# @lc code=end

