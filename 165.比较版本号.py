class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m, n = len(version1), len(version2)
        i, j = 0, 0
        while i < m or j < n:
            x = 0
            while i < m and version1[i] != '.':
                x = x * 10 + ord(version1[i]) - ord('0')
                i += 1
            i += 1
            y = 0
            while j < n  and version2[j] != '.':
                y = y * 10 + ord(version2[j]) - ord('0')
                j += 1
            j += 1
            if x > y: return 1
            elif x < y: return -1

        return 0
