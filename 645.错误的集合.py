lass Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, miss = -1, -1
        for n in nums:
            if nums[abs(n) - 1] < 0:
                dup = abs(n)
            else:
                nums[abs(n) - 1] *= -1
        
        for i, n in enumerate(nums):
            if n > 0:
                miss = i + 1
                break

        return [dup, miss]
