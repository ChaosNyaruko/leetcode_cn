#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (69.38%)
# Likes:    481
# Dislikes: 0
# Total Accepted:    64.7K
# Total Submissions: 93.2K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
# 
# 示例:
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");   
# trie.search("app");     // 返回 true
# 
# 说明:
# 
# 
# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。
# 
# 
#

# @lc code=start
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_string = False
        self.next = [None] * 26


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for c in word:
            c_ = ord(c) - ord("a")
            if not cur.next[c_]:
                cur.next[c_] = Trie()
            cur = cur.next[c_]
        cur.is_string = True
            


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for c in word:
            c_ = ord(c) - ord("a")
            if not cur.next[c_]:
                return False
            cur = cur.next[c_] 
        return cur.is_string


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self
        for c in prefix:
            c_ = ord(c) - ord("a")
            if not cur.next[c_]:
                return False
            cur = cur.next[c_]
        return True 



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

