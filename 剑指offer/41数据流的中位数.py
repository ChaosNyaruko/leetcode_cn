class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Biggers = [] # 小根堆
        self.Smallers = [] # 大根堆，注意要取相反的


    def addNum(self, num: int) -> None:
        # 优先插进少的那一堆
        # 优先插入大的一部分（小根堆）-> 先push到小的那一部分，再调整到大的那边去
        if len(self.Biggers) == len(self.Smallers):
            heapq.heappush(self.Biggers, -heapq.heappushpop(self.Smallers, -num))
        else:
            heapq.heappush(self.Smallers, -heapq.heappushpop(self.Biggers, num))





    def findMedian(self) -> float:
        return self.Biggers[0] if len(self.Biggers) != len(self.Smallers) else (self.Biggers[0] - self.Smallers[0])/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()