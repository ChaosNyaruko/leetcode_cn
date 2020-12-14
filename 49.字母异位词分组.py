#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            m[key].append(word)
        return list(m.values())
# @lc code=end

