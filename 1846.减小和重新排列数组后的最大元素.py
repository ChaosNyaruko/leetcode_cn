class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff != 0:
                arr[i] = arr[i - 1] + 1

        return min(len(arr), arr[-1])
