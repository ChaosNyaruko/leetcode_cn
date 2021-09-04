class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        MOD = 10 ** 9 + 7
        f0, f1 = 0, 1
        for i in range(2, n + 1):
            f0, f1 = f1, f0 + f1
            # f1, f0 = f0 + f1, f1
            # print(i, f0, f1)

        return f1 % MOD
