#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        cnt = dict()
        for num in nums:
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1
        heapq.heapify(freq)
        
        for num, c in cnt.items():
            if len(freq) == k:
                heapq.heappushpop(freq, (c, num))
            else:
                heapq.heappush(freq, (c, num))
        res = []
        while freq:
            res.append(freq[0][1])
            heapq.heappop(freq)
        return res

# @lc code=end

