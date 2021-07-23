class Solution:
    def maximumTime(self, time: str) -> str:
        res = list(time)
        for i, c in enumerate(res):
            if c != '?':
                continue
            if i == 0:
                res[i] = '2' if res[i+1] == '?' or '0' <= res[i+1] <= '3' else '1' 
            elif i == 1:
                res[i] = '3' if res[i-1]=='2' else '9'
            elif i == 3:
                res[i] = '5'
            elif i == 4:
                res[i] = '9'

        return ''.join(res)

