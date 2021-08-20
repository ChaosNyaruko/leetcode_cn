class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        t = list(s)
        for i in range(0, len(s), 2*k):
            t[i:i+k] = reversed(t[i:i+k])

        return ''.join(t)

