class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(x):
            return x in 'aeiouAEIOU'
        _s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not isVowel(_s[l]):
                l += 1
            while l < r and not isVowel(_s[r]):
                r -= 1
            if l < r:
                _s[l], _s[r] = _s[r], _s[l]
                l += 1
                r -= 1
        
        return ''.join(_s)
