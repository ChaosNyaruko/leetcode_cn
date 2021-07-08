class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = -1
        cnt = 0
        for n in nums:
            if cnt == 0:
                cur = n
                cnt += 1
            elif n == cur:
                cnt += 1
            else:
                cnt -= 1
        
        cnt = 0
        for n in nums:
            if n == cur:
                cnt += 1
        
        return -1 if 2 * cnt <= len(nums) else cur
