class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(days):
            flowers, bouquets = 0, 0
            for i, d in enumerate(bloomDay):
                if d <= days:
                    flowers += 1
                    if flowers == k:
                        flowers = 0
                        bouquets += 1
                        if bouquets == m:
                            break
                else:
                    flowers = 0

            return bouquets == m
        
        if len(bloomDay) < k * m:
            return -1

        l, r = 1, max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
