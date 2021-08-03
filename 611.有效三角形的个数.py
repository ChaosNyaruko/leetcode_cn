class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res =0
        for i in range(n - 2):
            k = i
            for j in range(i + 1, n - 1):
                while k + 1 < n and nums[i] + nums[j] > nums[k + 1]:
                    k += 1
                
                res += max(k - j, 0)

        return res
