class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        factor = [2,3,5]
        for f in factor:
            while n % f == 0:
                n //= f

        return n == 1
