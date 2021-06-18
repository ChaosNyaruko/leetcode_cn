class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []
        for word in arr:
            mask = 0
            for c in word:
                idx = ord(c) - ord('a')
                if (mask >> idx) & 1:
                    mask = 0
                    break
                mask |= 1 << idx
            if mask > 0:
                masks.append(mask)


        res = 0
        def countOne(a):
            ans = 0
            while a > 0:
                ans += 1
                a &= (a - 1)
            return ans

        def dfs(path, index):
            if index == len(masks):
                nonlocal res
                res = max(res, countOne(path))
                return
            # 选index
            if masks[index] & path == 0:
                dfs(path | masks[index], index+1)
            
            dfs(path, index+1)
            return
        dfs(0, 0)
        return res

