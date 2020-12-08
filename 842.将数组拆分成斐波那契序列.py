#
# @lc app=leetcode.cn id=842 lang=python3
#
# [842] 将数组拆分成斐波那契序列
#

# @lc code=start
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        res = list()
        def helper(index: int) -> bool:
            if index == len(S):
                return len(res) >= 3
            cur = 0
            for i in range(index, len(S)):
                if i > index and S[index] == '0':
                    break
                cur = cur * 10 + ord(S[i]) - ord('0')
                if cur > 2 ** 31 - 1:
                    break
                if len(res) < 2 or res[-1] + res[-2] == cur:
                    res.append(cur)
                    if helper(i + 1):
                        return True
                    res.pop()
                elif len(res) >= 2 and res[-1] + res[-2] < cur:
                    break
            return False
        helper(0)
        return res

            
            
        
# @lc code=end

