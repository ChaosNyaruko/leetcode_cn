#
# @lc app=leetcode.cn id=839 lang=python3
#
# [839] 相似字符串组
#
# https://leetcode-cn.com/problems/similar-string-groups/description/
#
# algorithms
# Hard (37.16%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 13.8K
# Testcase Example:  '["tars","rats","arts","star"]'
#
# 如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y
# 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。
# 
# 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与
# "tars"，"rats"，或 "arts" 相似。
# 
# 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts"
# 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
# 
# 给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["tars","rats","arts","star"]
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["omv","ovm"]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# sum(strs[i].length) 
# strs[i] 只包含小写字母。
# strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。
# 
# 
# 
# 
# 备注：
# 
# 字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。
# 
#

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.rank[rx] += self.rank[ry]
        self.count -= 1
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(a, b):
            diff = 0
            # words in strs are anagrams
            # don't need to check length
            for i in range(len(a)):
                if a[i] == b[i]:
                    continue
                diff += 1
                if diff > 2:
                    return False
            return True
        
        uf = UnionFind(len(strs))
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                # if uf.connected(i, j): # actually it will be faster without this judgement
                #     continue
                if not isSimilar(strs[i], strs[j]):
                    continue
                uf.union(i, j)
        return uf.count

                
# @lc code=end

