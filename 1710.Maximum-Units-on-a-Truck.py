class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        buckets = [-1 for _ in range(1001)]
        for boxType in boxTypes:
            if buckets[boxType[1]] == -1:
                buckets[boxType[1]] = boxType[0]
            else:
                buckets[boxType[1]] += boxType[0]

        res = 0
        for i in range(1000, -1, -1):
            if buckets[i] == -1:
                continue
            if buckets[i] > truckSize:
                res += truckSize * i
                return res
            else:
                res += buckets[i]*i
                truckSize -= buckets[i]

        return res
