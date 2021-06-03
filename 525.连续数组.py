class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        pos = dict()
        pos[0] = -1
        res = 0
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            if count in pos:
                res = max(i - pos[count], res)
            else:
                pos[count] = i

        return res

