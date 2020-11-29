class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        cnt = 0
        for i, val in enumerate(nums):
            if cnt == 0:
                cnt += 1
                majority = val
            elif majority == val:
                cnt += 1
            else:
                cnt -= 1
        return majority