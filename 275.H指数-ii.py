class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # the first element that satisfies citations[i] >= n - i
        n = len(citations)
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2
            if citations[m] < n - m:
                l = m + 1
            else:
                r = m
        
        return n - l if citations[l] >= n - l else 0
