#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        n = len(A)
        res = []
        for i in range(n - 1, -1 , -1) :
            sum = A[i] + K % 10
            K //= 10
            if sum >= 10:
                sum %= 10
                K += 1

            res.append(sum %10)

        while  K > 0:
            res.append(K % 10)
            K //= 10
        return res[::-1]
# @lc code=end

