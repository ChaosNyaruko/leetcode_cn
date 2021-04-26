class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def can(x):
            need = 1
            cur = 0
            for weight in weights:
                if cur + weight <= x:
                    cur += weight
                else:
                    cur = weight
                    need += 1
            return need <= D
        left, right = max(weights), sum(weights)
        # 使用二分找到可以在D天内运送完的最低要求运力
        while left < right:
            m = left + (right - left) // 2
            if can(m):
                right = m
            else:
                left = m + 1

        return left
