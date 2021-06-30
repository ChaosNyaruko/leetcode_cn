class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dp = [0 for _ in range(n)]
        dp[0]= 1
        for i in range(k):
            next = [0 for _ in range(n)]
            for edge in relation:
                src, dst = edge[0], edge[1]
                next[dst] += dp[src] 
            dp = next
        return dp[n - 1]
