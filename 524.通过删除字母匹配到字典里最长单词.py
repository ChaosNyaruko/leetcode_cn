class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key = lambda x: (-len(x), x))

        maxLen = 0
        res = ""
        for t in dictionary:
            i, j = 0,0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    j += 1
                i += 1

            if j == len(t) and (len(t) > maxLen or len(t) == maxLen and t < res):
                maxLen, res = len(t), t

        return res
