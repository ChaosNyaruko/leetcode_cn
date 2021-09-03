class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        hp = []
        for i in range(len(arr)):
            if len(hp) < k:
                heapq.heappush(hp, -arr[i])
            else:
                heapq.heappush(hp, -arr[i])
                heapq.heappop(hp)

        return [-x for x in hp]
