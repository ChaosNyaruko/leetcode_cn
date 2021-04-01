class Solution:
    def clumsy(self, N: int) -> int:
        stk = [N]
        oper = 0
        N -= 1
        while N > 0:
            if oper % 4 == 0:
                stk.append(stk.pop() * N)
            elif oper % 4 == 1:
                top = stk.pop()
                tmp = abs(top) // N
                if top < 0:
                    tmp = -tmp
                stk.append(tmp)
            elif oper % 4 == 2:
                stk.append(N)
            else:
                stk.append(-N)
            N -= 1
            oper += 1
        return sum(stk)

if __name__ == '__main__':
    sl = Solution()
    res = sl.clumsy(10)
    print(res)