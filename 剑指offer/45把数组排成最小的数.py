class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def mycmp(a, b) -> bool:
            str1 = str(a)+str(b)
            str2 = str(b)+str(a)
            if str1 > str2:
                return 1
            elif str1 < str2:
                return -1
            else:
                return 0
        # sorted(nums, key=functools.cmp_to_key(mycmp))
        nums.sort(key=functools.cmp_to_key(mycmp))
       # print(nums)
        strs = [str(num) for num in nums]
        return ''.join(strs)