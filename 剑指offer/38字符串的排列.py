class Solution:
    def permutation_1(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c)) # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i] # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1) # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i] # 恢复交换
        dfs(0)
        return res

    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        c.sort()
        visited = [False] * len(c)
        # print(visited)
        path = []
        def dfs(x, c, visited: List[bool]):
            # print("x=", x, visited)
            if x == len(c):
                res.append(''.join(path))
                return
            for i in range(0, len(c)):
                if visited[i] or (i > 0 and c[i] == c[i-1] and not visited[i-1]):
                    continue
                visited[i] = True
                path.append(c[i])
                dfs(x+1, c, visited)
                visited[i] = False
                del path[-1]
            return
        dfs(0, c, visited)
        return res
