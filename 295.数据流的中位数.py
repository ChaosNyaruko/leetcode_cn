#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # 大根堆，存储较小的一半数（python的heapq只有小根堆，所以存相反数）
        self.big = [] # 小根堆， 存储较大的一半数



    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.big, -heapq.heappop(self.small))
        if len(self.small) < len(self.big):
            heapq.heappush(self.small, -heapq.heappop(self.big)) 

    def findMedian(self) -> float:
        return -self.small[0] if len(self.small) > len(self.big) else (self.big[0]-self.small[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

