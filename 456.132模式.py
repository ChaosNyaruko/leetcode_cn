class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        max_k = -2**32
        cand = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < max_k:
                return True
            while cand and nums[i] > cand[-1]:
                max_k = max(max_k, cand.pop())
            if not cand or cand[-1] > nums[i]:
                cand.append(nums[i])

        return False
