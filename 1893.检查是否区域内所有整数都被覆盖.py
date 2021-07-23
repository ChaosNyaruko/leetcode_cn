class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0 for _ in range(52)]
        # diff[i] 覆盖i的区间个数和覆盖i - 1的区间个数的差值
        for interval in ranges:
            diff[interval[0]] += 1
            diff[interval[1] + 1] -= 1

        cur = 0
        for i in range(len(diff)):
            cur += diff[i]
            if i >= left and i <= right and cur <=0:
                return False

        return True

