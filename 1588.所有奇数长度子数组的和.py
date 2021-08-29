class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i, x in enumerate(arr):
            left, right = i + 1, len(arr) - i
            leftOdd, rightOdd = left // 2,  right // 2
            leftEven, rightEven = (left + 1) // 2, (right + 1) // 2
            res += x * (leftOdd * rightOdd + leftEven * rightEven)
        
        return res
