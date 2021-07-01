class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        buckets = [0 for _ in range(100000+1)]
        for cost in costs:
            buckets[cost] += 1
        
        res = 0
        remain = coins
        for c in range(0, 100000+1):
            #print(remain, c, buckets[c])
            if buckets[c] > 0:
                cur = buckets[c] * c
                if remain > cur:
                    remain -= cur
                    res += buckets[c]
                else:
                    res += remain // c
                    #print("return in",res)
                    return res
        
        return res
