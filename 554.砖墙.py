class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cnt = defaultdict(int)
        for w in wall:
            n = len(w)
            right_edge = 0
            for i in range(n - 1):
                right_edge += w[i]
                cnt[right_edge] += 1

        maxCnt = 0
        for k ,v in cnt.items():
            maxCnt = max(maxCnt, v)

        return len(wall) - maxCnt

