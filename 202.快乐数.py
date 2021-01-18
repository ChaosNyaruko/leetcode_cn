#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            res = 0
            while n > 0:
                n, remainer = divmod(n, 10)
                res += remainer ** 2
            return res
        slow = n
        fast = getNext(n) 
        while fast != 1 and slow != fast:
            # print("before", slow, fast)
            slow = getNext(slow)
            fast = getNext(getNext(fast))
            # print("after", slow, fast)
        return fast == 1
# @lc code=end

