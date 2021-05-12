class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        preXor = [0]
        for i in range(0, len(arr)):
            preXor.append(preXor[-1] ^ arr[i])

        res = []
        for query in queries:
            res.append(preXor[query[0]] ^ preXor[query[1] + 1])

        return res
