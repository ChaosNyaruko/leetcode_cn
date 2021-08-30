class Solution:

    def __init__(self, w: List[int]):
        self.pre = [0] * len(w)
        self.pre[0] = w[0]
        for i in range(1, len(w)):
            self.pre[i] = self.pre[i - 1] + w[i]
        
    def pickIndex(self) -> int:
        total = self.pre[-1]
        l, r = 0, len(self.pre)
        x = random.randint(1, total)
        while l < r:
            m = l + (r - l) // 2
            if self.pre[m] < x:
                l = m + 1
            else:
                r = m

        return l    




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
