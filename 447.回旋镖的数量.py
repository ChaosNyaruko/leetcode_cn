class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def dis(x, y):
            a = x[0] - y[0]
            b = x[1] - y[1]
            return a * a + b * b

        res = 0
        for p in points:
            d = defaultdict(int)

            for x in points:
                d[dis(p,x)] += 1

            for m in d.values():
                res += m * (m - 1)

        return res



