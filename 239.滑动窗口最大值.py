#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []
        for i in range(0, len(nums)):
            if  deque and i - deque[0] == k:
                deque.popleft()
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
            if i - k + 1 >= 0:
                res.append(nums[deque[0]])
        return res
# @lc code=end

