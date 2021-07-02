class Solution:
    def frequencySort1(self, s: str) -> str:
        freq = collections.Counter(s)
        buckets = [[] for _ in range(len(s) + 1)]
        for ch, f in freq.items():
            buckets[f].append(ch)

        res = ""
        for i in range(len(s), -1, -1):
            if buckets[i]:
                for c in buckets[i]:
                    res += c * i

        return res
    
    def frequencySort2(self, s: str) -> str:
        freq = dict()
        for i, c in enumerate(s):
            if c not in freq:
                freq[c] = (1, i)
            else:
                freq[c] = (freq[c][0] + 1, freq[c][1])
        items = freq.items()
        #print(items)
        pq = [(-y[0], y[1]) for _, y in items]
        heapq.heapify(pq)
        res = ""
        while pq:
            cur = heapq.heappop(pq)
            #print(cur)
            res += -cur[0] * s[cur[1]]
        return res
