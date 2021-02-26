#
# @lc app=leetcode.cn id=1178 lang=python3
#
# [1178] 猜字谜
#
# https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle/description/
#
# algorithms
# Hard (30.61%)
# Likes:    79
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 9.4K
# Testcase Example:  '["aaaa","asas","able","ability","actt","actor","access"]\n' +
  '["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]'
#
# 外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
#
# 字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：
#
#
# 单词 word 中包含谜面 puzzle 的第一个字母。
# 单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
# 例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而
# "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
#
#
# 返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i]
# 所对应的谜底的单词数目。
#
#
#
# 示例：
#
# 输入：
# words = ["aaaa","asas","able","ability","actt","actor","access"],
# puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# 输出：[1,1,3,2,4,0]
# 解释：
# 1 个单词可以作为 "aboveyz" 的谜底 : "aaaa"
# 1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
# 3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
# 2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
# 4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
# 没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。
#
#
#
#
# 提示：
#
#
# 1 <= words.length <= 10^5
# 4 <= words[i].length <= 50
# 1 <= puzzles.length <= 10^4
# puzzles[i].length == 7
# words[i][j], puzzles[i][j] 都是小写英文字母。
# 每个 puzzles[i] 所包含的字符都不重复。
#
#
#

# @lc code=start
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        freq = collections.Counter()
        for word in words:
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - ord("a")))
            if str(mask).count("1") <= 7:
                freq[mask] += 1

        res = []
        for puzzle in puzzles:
            total = 0
            mask = 0
            for i in range(1, 7):
                mask |= (1 << (ord(puzzle[i]) - ord("a")))

            subset = mask
            while subset: # 这种判断方式漏掉了0，即空集
                s = subset | (1 << (ord(puzzle[0]) - ord("a")))
                if s in freq:
                    total += freq[s]
                subset = (subset - 1) & mask

            null = (1 << (ord(puzzle[0]) - ord("a")))
            if null in freq:
                total += freq[null]
            res.append(total)

        return res
# @lc code=end

