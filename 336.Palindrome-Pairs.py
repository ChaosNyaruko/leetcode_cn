class TrieNode:
    def __init__(self):
        self.index = -1
        self.list = []
        self.next = [None for _ in range(26)]
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(s, start, end):
            l, r = start, end
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        root = TrieNode()
        res = []
        def addWord(w, index):
            p = root
            for i in range(len(w) - 1, -1, -1):
                j = ord(w[i]) - ord('a')
                if not p.next[j]:
                    p.next[j] = TrieNode()
                if isPalindrome(w, 0, i):
                    p.list.append(index)
                p = p.next[j]
            
            p.index = index
            p.list.append(index)
        
        def search(i):
            p = root
            for j in range(0, len(words[i])):
                n = ord(words[i][j]) - ord('a')
                if p.index >= 0 and p.index != i and isPalindrome(words[i], j, len(words[i]) - 1):
                    res.append([i, p.index])
                p = p.next[n]
                if not p:
                    return
            
            for j in p.list:
                if i == j:
                    continue
                res.append([i, j])
                    
                
        # build
        for i, word in enumerate(words):
            addWord(word, i)
            
        #search
        # ab dcba(abcd)
        for i in range(len(words)):
            search(i)
            
        return res
        
