class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        s = [0]
        for num in arr:
            s.append(s[-1] ^ num)

        cnt, total = Counter(), Counter()
        res = 0
        for k in range(len(arr)):
            if s[k + 1] in cnt:
                res += cnt[s[k+1]] * k - total[s[k+1]]
            cnt[s[k]] += 1
            total[s[k]] += k

        return res

