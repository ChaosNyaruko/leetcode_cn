from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        nums.sort()
        def dfs(start):
            # print("dfs", start, path)
            res.append(path.copy())
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                if i > start and nums[i - 1] == nums[i]:
                    continue
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
            return
        dfs(0)
        return res

if __name__ == '__main__':
    sl = Solution()
    res = sl.subsetsWithDup([1,2,2])
    print(res)
