class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        dead = set(deadends)
        if '0000' in dead:
            return -1

        def plusOne(c):
            return '0' if c == '9' else str(int(c) + 1)
        def minusOne(c):
            return '9' if c == '0' else str(int(c) - 1)
        
        def get(status):
            s = list(status)
            for i in range(4):
                num = s[i]
                s[i] = minusOne(num)
                yield ''.join(s)
                s[i] = plusOne(num)
                yield ''.join(s)
                s[i] = num
        
        seen = {'0000'}
        q = deque([('0000',0)])
        while q:
            status, step = q.popleft()
            for nextStatus in get(status):
                if nextStatus not in seen and nextStatus not in dead:
                    if nextStatus == target:
                        return step + 1
                    else:
                        q.append((nextStatus, step+1))
                        seen.add(nextStatus)
        return -1
