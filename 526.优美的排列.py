class Solution:
    def countArrangement(self, n: int) -> int:
        def countOne(x):
            res = 0
            while x > 0:
                res += 1
                x &= x - 1

            return res

        f = [0] * (1 << n)
        f[0] = 1
        for mask in range(1<<n):
            index = countOne(mask)
            for i in range(n):
                if mask & (1 << i) and ((i + 1) % index == 0 or index % (i + 1) == 0):
                    f[mask] += f[mask ^ (1 << i)]

        return f[-1]
