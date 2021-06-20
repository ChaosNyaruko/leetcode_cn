class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def countOne(n):
            res = 0
            while n:
                res += 1
                n &= (n - 1)
            return res

        res = []
        for h in range(12):
            for m in range(60):
                if countOne(h)+countOne(m)==turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res

