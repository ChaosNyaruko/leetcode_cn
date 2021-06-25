class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 0 1 2
        # 3 4 5
        dirs = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
        start = ''
        target = '123450'
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])
        
        q = deque([start])
        res = 0
        seen = set()
        seen.add(start)
        while q:
            for _ in range(len(q)-1, -1, -1):
                cur = q.popleft()
                #print(cur)
                if cur == target:
                    return res
                zeroIndex = cur.find('0')
                possibleDir = dirs[zeroIndex]
                for d in possibleDir:
                    s = list(cur)
                    s[zeroIndex], s[d] = s[d], s[zeroIndex]
                    nextState = ''.join(s)
                    if nextState not in seen:
                        print(nextState)
                        seen.add(nextState)
                        q.append(nextState)
            res += 1
        return -1
