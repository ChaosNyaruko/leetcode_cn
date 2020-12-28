#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stk = []
        res = [0] * len(T)
        for i, num in enumerate(T):
            # delta = 1
            while stk and num > T[stk[-1]]:
                top = stk.pop()
                res[top] = i - top 
                # res[top] = delta
                # delta += 1
            stk.append(i)
        return res

        
# @lc code=end

