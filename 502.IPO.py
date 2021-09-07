class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        arr = [(capital[i], profits[i]) for i in range(n)]

        arr.sort(key= lambda x: x[0])

        cur = 0
        pq = []
        for _ in range(k):
            while cur < n and arr[cur][0] <= w:
                heapq.heappush(pq, -arr[cur][1])
                cur += 1
            
            if pq:
                w -= heapq.heappop(pq)
            else:
                break
        
        return w
