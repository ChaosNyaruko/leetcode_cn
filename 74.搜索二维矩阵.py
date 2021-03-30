class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l < r:
            m = l + (r - l + 1) // 2
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m
        if matrix[l][0] > target:
            return False

        row = l
        l, r = 0, len(matrix[row]) - 1
        while l < r:
            m = l + (r - l) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return True if matrix[row][l] == target else False



