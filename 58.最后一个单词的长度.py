class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p = 0
        res = 0
        for c in s:
            if c == ' ':
                res = p if p > 0 else res
                p = 0
            else:
                p += 1
        
        res = p if p > 0 else res
        return res
