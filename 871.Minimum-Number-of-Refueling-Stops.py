class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, float('inf')])
        pq = []
        tank = startFuel
        res = 0
        prev = 0
        for i in range(len(stations)):
            location, fuel = stations[i]
            tank -= location - prev
            while pq and tank < 0:
                tank += -heapq.heappop(pq)
                res += 1
            if tank < 0:
                return -1
            prev = location
            heapq.heappush(pq,-fuel)
        
        return res

