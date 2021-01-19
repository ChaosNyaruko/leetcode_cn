#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution:
    class TrieNode:
        def __init__(self):
            self.word = ""
            self.next = [None] * 26 

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def buildTree(words):
            root = self.TrieNode()
            for word in words:
                p = root
                for c in word:
                    n = ord(c) - ord("a")
                    if p.next[n] == None: p.next[n] = self.TrieNode()
                    p = p.next[n]
                p.word = word
            return root
        res = []
        def dfs(i, j, p):
            c = board[i][j]
            if c == '#' or p.next[ord(c) - ord('a')] == None:
                return
            p = p.next[ord(c) - ord('a')]
            if p.word != "":
                res.append(p.word)
                p.word = "" # 防止重复
            board[i][j] = '#'

            if i > 0: dfs(i - 1, j, p)
            if j > 0: dfs(i, j - 1, p)
            if i < len(board) - 1: dfs(i + 1, j, p)
            if j < len(board[0]) - 1: dfs(i, j + 1, p)
            board[i][j] = c
            return
        root = buildTree(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)

        return res
# @lc code=end

