class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [[-1000000 for _ in range(target + 1)] for _ in range(10)]
        dp[0][0] = 0
        source = [[10 for _ in range(target+1)] for _ in range(10)]
        for i in range(1, len(cost) + 1):
            c = cost[i - 1]
            for j in range(0, target+1):
                #print(i, j, c)
                if j < c:
                    dp[i][j] = dp[i -1][j]
                    source[i][j] = j
                else:
                    if dp[i - 1][j] <= dp[i][j -c] +1:
                        dp[i][j] = dp[i][j-c] +1
                        source[i][j] = j - c
                    else:
                        dp[i][j] = dp[i - 1][j]
                        source[i][j] = j

        if dp[9][target] < 0:
            return '0'
        res = ""
        i, j = 9, target
        while i > 0:
            if j == source[i][j]:
                i -= 1
            else:
                j = source[i][j]
                res += str(i)
        return res

