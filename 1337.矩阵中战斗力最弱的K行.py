class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        rows = []
        for i in range(m):
            l, r = 0, n - 1
            while l < r:
                mid = l + (r - l) // 2
                # find the first 0
                if mat[i][mid] == 1:
                    l = mid + 1
                else:
                    r = mid    

            pos = l if mat[i][l] == 0 else l + 1 
            rows.append((pos, i))
        
        res = []
        heapq.heapify(rows)
        for _ in range(k):
            x = heapq.heappop(rows)
            res.append(x[1])

        return res
