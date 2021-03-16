class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row, col = 0, -1
        res = [[0 for _ in range(n)] for _ in range(n)]
        r, c = n, n
        v = 0
        while True:
            for i in range(c):
                col += 1
                v += 1
                res[row][col] = v

            r -= 1
            if r == 0:
                break

            for i in range(r):
                row += 1
                v += 1
                res[row][col] = v

            c -= 1
            if c == 0:
                break

            for i in range(c):
                col -= 1
                v += 1
                res[row][col] = v

            r -= 1
            if r == 0:
                break
            for i in range(r):
                row -= 1
                v += 1
                res[row][col] = v

            c -= 1
            if c == 0:
                break
        return res
