class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        for i in range(2, n + 1):
            if i * i > n:
                break
            while n % i == 0:
                res += i
                n //= i
        if n > 1:
            res += n
        
        return res
