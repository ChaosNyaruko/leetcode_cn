class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, floor(sqrt(c))
        while left <= right:
            s = left * left + right * right
            if s == c:
                return True
            elif s > c:
                right -= 1
            else:
                left += 1

        return False
