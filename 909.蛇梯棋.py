class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        def index(x, y):
            if x & 0x1 == 1: # even
                return (N -1 - x) * N + y + 1 
            else:
                return (N - 1 - x) * N + (N - 1 -y) + 1
        
        def grid(x):
            r = (x - 1) // N
            c = (x - 1) % N
            if r & 0x1 == 1:
               c = N -1 - c 
            return N - 1 - r, c
        '''
        for r in range(0, N):
            for c in range(0, N):
                print(index(r,c),end=' ')
            print()
        '''
        '''
        for num in range(1, N*N+1):
            print(grid(num), end=' ')
            if num % N == 0:
                print()
        '''
        seen = set()
        q = deque([1])
        seen.add(1)
        step = 0
        while q:
            for _ in range(len(q), 0, -1):
                cur = q.popleft()
                if cur == N * N:
                    return step
                for i in range(1, 7):
                    next_ = cur + i
                    if next_ > N * N:
                        continue
                    r, c = grid(next_)
                    # print("step:", step, "next_:", next_, "grid:", (r,c), "b[r][c]", board[r][c])
                    if board[r][c] > 0:
                        next_ = board[r][c]
                    if next_ not in seen:
                        # print("step:",step, "append:", next_)
                        q.append(next_)
                    seen.add(next_)
            step += 1
        return -1
