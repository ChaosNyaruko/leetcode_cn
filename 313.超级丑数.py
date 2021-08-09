class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m = len(primes)
        dp = [0] * (n + 1)
        dp[1] = 1
        pointers = [1] * m

        for i in range(2, n + 1):
            dp[i] = minDp = min(dp[pointers[j]] * primes[j] for j in range(m))

            for j in range(m):
                if dp[pointers[j]] * primes[j] == minDp:
                    pointers[j] += 1

        return dp[n]

