class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        res = 0
        for c in s:
            if c == 'L':
                l += 1
            else:
                l -= 1
            
            if l == 0:
                res += 1
        
        return res
