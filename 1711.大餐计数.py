class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        n = len(deliciousness)
        MOD = 1000000007
        res = 0
        maxSum = 2 * max(deliciousness)
        counter = collections.defaultdict(int)
        for i in range(n):
            s = 1
            while s <= maxSum:
                res = (res + counter[s - deliciousness[i]]) % MOD
                s <<= 1
            counter[deliciousness[i]] += 1

        
        return res
