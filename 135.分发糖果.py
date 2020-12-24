#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy_1(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0] * n
        for i in range(n):
            if i > 0 and ratings[i-1] < ratings[i]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 1

        res = right = 0
        for i in range(n-1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i+1]:
                right = right + 1
            else:
                right = 1
            res += max(right, left[i])
        return res

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ret = 1
        inc, dec, pre = 1, 0, 1

        # 1 3 5 3 2 1
        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                dec = 0
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                ret += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    # print("dec=inc", inc, "r[i]=", ratings[i], i)
                    dec += 1
                ret += dec
                pre = 1
        
        return ret

# @lc code=end

