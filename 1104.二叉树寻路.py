class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        row, rowStart = 1, 1
        while rowStart * 2 <= label:
            row += 1
            rowStart *= 2

        def getReverse(row, label):
            return (1 << (row - 1)) +  (1 << row) - 1 - label

        if row % 2 == 0:
            label = getReverse(row, label)

        res = []
        while row > 0:
            if row % 2 == 0:
                res.append(getReverse(row, label))
            else:
                res.append(label)

            label >>= 1
            row -= 1

        return res[::-1]
