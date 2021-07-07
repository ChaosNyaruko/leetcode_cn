class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        s = collections.defaultdict(int)
        s[0] = 1
        cur = 0
        res = 0
        for n in nums:
            cur += n
            res += s[cur - goal]
            s[cur] += 1
        return res
