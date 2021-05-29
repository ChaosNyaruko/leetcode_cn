
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def subarrayK(nums, k):
            cnt = defaultdict(int)
            pre = 0
            res = 0
            cnt[0] = 1
            for num in nums:
                pre += num
                if pre - k in cnt:
                    res += cnt[pre - k]
                cnt[pre] += 1
                
            
            return res
        
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            s = [0 for _ in range(n)]
            for j in range(i, m):
                for c in range(n):
                    s[c] += matrix[j][c]
                res += subarrayK(s, target)
        
        return res
