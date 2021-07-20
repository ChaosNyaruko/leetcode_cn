class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            a1, a2 = firstList[i][0], firstList[i][1]
            b1, b2 = secondList[j][0], secondList[j][1]

            if b1 <= a2 and a1 <= b2:
              res.append([max(a1,b1), min(a2, b2)])

            if a2 <= b2:
                i += 1
            else:
                j += 1

        return res

