class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = collections.defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))



    def get(self, key: str, timestamp: int) -> str:
        s = self.m[key]
        l, r = 0, len(s) - 1
        while l < r:
            m = l + (r - l + 1) // 2
            if s[m][0] > timestamp:
                r = m - 1
            else:
                l = m
        if l >= len(s) or s[l][0] > timestamp:
            return ''
        return s[l][1]  



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
