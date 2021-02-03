#
# @lc app=leetcode.cn id=480 lang=python3
#
# [480] 滑动窗口中位数
#
# https://leetcode-cn.com/problems/sliding-window-median/description/
#
# algorithms
# Hard (40.02%)
# Likes:    152
# Dislikes: 0
# Total Accepted:    8.6K
# Total Submissions: 21.5K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。
#
# 例如：
#
#
# [2,3,4]，中位数是 3
# [2,3]，中位数是 (2 + 3) / 2 = 2.5
#
#
# 给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1
# 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。
#
#
#
# 示例：
#
# 给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。
#
# 窗口位置                      中位数
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
# ⁠1 [3  -1  -3] 5  3  6  7      -1
# ⁠1  3 [-1  -3  5] 3  6  7      -1
# ⁠1  3  -1 [-3  5  3] 6  7       3
# ⁠1  3  -1  -3 [5  3  6] 7       5
# ⁠1  3  -1  -3  5 [3  6  7]      6
#
#
# 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。
#
#
#
# 提示：
#
#
# 你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。
# 与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。
#
#
#

# @lc code=start
class DualHeap:
    def __init__(self, k):
        self.k = k
        self.delayed = collections.Counter()
        self.smaller = list() # 较小的一半，大根堆
        self.bigger = list() # 较大的一半，小根堆
        self.smallerSize = 0 # exclude delayed elements
        self.biggerSize = 0 # exclude delayed elements

    # 不断弹出一个堆，直到堆顶元素不是“延迟删除”的
    def prune(self, heap):
        while heap:
            num = heap[0]
            if heap is self.smaller:
                num = -num
            if num in self.delayed:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    self.delayed.pop(num)
                heapq.heappop(heap)
            else:
                return

    # 令smaller和bigger保持smallerSize = biggerSize / biggerSize + 1的状态
    def makeBalance(self):
        if self.smallerSize > self.biggerSize + 1:
            heapq.heappush(self.bigger, -self.smaller[0])
            heapq.heappop(self.smaller)
            self.smallerSize -= 1
            self.biggerSize += 1
            self.prune(self.smaller)
        elif self.smallerSize < self.biggerSize:
            heapq.heappush(self.smaller, -self.bigger[0])
            heapq.heappop(self.bigger)
            self.smallerSize += 1
            self.biggerSize -= 1
            self.prune(self.bigger)

    def insert(self, num):
        if not self.smaller or -self.smaller[0] >= num:
            heapq.heappush(self.smaller, -num)
            self.smallerSize += 1
        else:
            heapq.heappush(self.bigger, num)
            self.biggerSize += 1
        self.makeBalance()

    def erase(self, num):
        self.delayed[num] += 1
        if num <= -self.smaller[0]:
            self.smallerSize -= 1
            if num == -self.smaller[0]:
                self.prune(self.smaller)
        else:
            self.biggerSize -= 1
            if num == self.bigger[0]:
                self.prune(self.bigger)
        self.makeBalance()

    def getMedian(self):
        return -self.smaller[0] if self.k % 2 == 1 else (self.bigger[0] - self.smaller[0]) / 2

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DualHeap(k)
        for num in nums[:k]:
            dh.insert(num)

        res = [dh.getMedian()]
        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i - k])
            res.append(dh.getMedian())

        return res
# @lc code=end

