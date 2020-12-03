#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True for x in range(0, n)]
        # print(isPrime)
        cnt = 0
        for x in range(2, n):
            # print("x:",x)
            if isPrime[x]:
                cnt += 1
                '''
                filterNum = x * x
                while filterNum < n:
                    isPrime[filterNum] = False
                    filterNum += x
                '''
                for y in range(x * x, n, x):
                    isPrime[y] = False
        return cnt

# @lc code=end

