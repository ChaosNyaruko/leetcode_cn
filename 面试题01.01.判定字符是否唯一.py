class Solution:
    def isUnique(self, astr: str) -> bool:
        mask = 0
        for c in astr:
            x = ord(c) - ord('a')
            if mask & (1 << x) :
                return False
            else:
                mask |= (1 << x)
        
        return True
