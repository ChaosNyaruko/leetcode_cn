class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 0, 0, 0
        dp = [1]
        while n > 1:
            n2, n3, n5 = dp[p2] * 2, dp[p3] * 3, dp[p5] *5
            num = min(n2, n3, n5)
            if num == n2:
                p2 += 1
            if num == n3:
                p3 += 1
            if num == n5:
                p5 += 1
            n -= 1
            dp.append(num)
        return dp[-1]

