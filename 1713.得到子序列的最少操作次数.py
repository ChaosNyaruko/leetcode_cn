class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        pos = dict()
        for i, t in enumerate(target):
            pos[t] = i

        d = []
        for v in arr:
            if v in pos:
                idx = pos[v]

                # LIS
                if not d or idx > d[-1]:
                    d.append(idx)
                else:
                    l, r = 0, len(d) - 1
                    # find the first element that >= idx, and replace it with idx
                    while l < r:
                        m = l + (r - l) // 2
                        if d[m] < idx:
                            l = m + 1
                        else:
                            r = m
                    d[l] = idx

        return len(target) - len(d)

