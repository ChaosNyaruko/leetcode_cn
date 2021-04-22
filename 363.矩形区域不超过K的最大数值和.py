from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float("-inf")
        for i in range(m):
            sum_ = [0] * n
            for j in range(i, m):
                for c in range(n):
                    sum_[c] += matrix[j][c]

                set_ = SortedList([0])
                sr = 0
                for v in sum_:
                    sr += v
                    min_sl = set_.bisect_left(sr - k)
                    if min_sl != len(set_):
                        ans = max(ans, sr - set_[min_sl])
                    set_.add(sr)

        return ans

