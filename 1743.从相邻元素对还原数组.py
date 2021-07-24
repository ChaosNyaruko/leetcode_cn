class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjs = collections.defaultdict(list)

        for edge in adjacentPairs:
            adjs[edge[0]].append(edge[1])
            adjs[edge[1]].append(edge[0])
        n = len(adjacentPairs) + 1
        res = [0] * n

        for e in adjs.items():
            if len(e[1]) == 1:
                res[0] = e[0]
                break

        res[1] = adjs[res[0]][0]
        for i in range(2, n):
            x = adjs[res[i - 1]]
            res[i] = x[0] if res[i-2] == x[1] else x[1]



        return res


