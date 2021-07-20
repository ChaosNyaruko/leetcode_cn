class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def cmp(x, y):
            if x[0] == y[0]:
                return y[1] - x[1]
            return x[0] - y[0]

        intervals = sorted(intervals, key=cmp_to_key(cmp))

        left, right = intervals[0][0], intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[1] <= right:
                res += 1
            elif cur[0] <= right:
                right = cur[1]
            elif cur[0] >  right:
                left, right = cur[0], cur[1]
            else:
                print("bad case")

        return len(intervals) - res

