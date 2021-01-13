#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

import functools
from typing import List
# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def mycmp(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1
        # s = list(map(str, nums))
        s = map(str, nums)
        # print("s1", list(s))
        # print("s2", list(s))
        # test = sorted(nums, key= functools.cmp_to_key(lambda x, y: mycmp(str(x), str(y))))
        # testStr = ''.join(map(str, test))
        # return '0' if testStr[0] == '0' else testStr
        largest = sorted(s, key= functools.cmp_to_key(mycmp))
        largest = ''.join(largest)
        return '0' if largest[0] == '0' else largest
# @lc code=end


nums = [10, 2]#[10] #[1] #[3,30,34,5,9] #[10,2]
sl = Solution()
res = sl.largestNumber(nums)
print(res)