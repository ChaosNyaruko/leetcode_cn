class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        right, n = 0, len(words)
        res = []
        while True:
            l = 0
            left = right
            while right < n and l + len(words[right]) + right - left <= maxWidth:
                l += len(words[right])
                right += 1
            
            if right == n: # last line
                s = ' '.join(words[left:right]) #  + ' ' * (maxWidth - len(s))
                res.append(s + ' ' * (maxWidth - len(s)))
                break
            
            numWords = right -left
            numSpaces = maxWidth - l
            if numWords == 1:
                s = words[left] + ' ' * numSpaces
                res.append(s)
                continue

            avgSpaces = numSpaces // (numWords - 1)
            extraSpace = numSpaces % (numWords - 1)
            s1 = (' ' * (avgSpaces + 1)).join(words[left: left + extraSpace + 1])
            s2 = (' ' * avgSpaces).join(words[left + extraSpace + 1:right])
            s = s1 + ' ' * avgSpaces + s2
            res.append(s)
        
        return res
