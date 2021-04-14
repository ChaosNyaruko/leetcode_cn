class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.isword = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self
        for c in word:
            if p.children[ord(c) - ord('a')]:
                pass
            else:
                p.children[ord(c) - ord('a')] = Trie()
            p = p.children[ord(c) - ord('a')]
        p.isword = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self
        for c in word:
            if not p.children[ord(c) - ord('a')]:
                return False
            p = p.children[ord(c) - ord('a')]
        return p.isword

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self
        for c in prefix:
            if not p.children[ord(c) - ord('a')]:
                return False
            p = p.children[ord(c) - ord('a')]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
