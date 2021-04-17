class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        d = dict()
        bucket_size = t + 1
    
        def getid(n):
            if n >= 0:
                return n // bucket_size
            return int((n + 1) / bucket_size) - 1 # 向零取整，// 与其他语言的区别

        for i, n in enumerate(nums):
            bucket_index = getid(n) 
            if bucket_index in d:
                return True
            if bucket_index - 1 in d and abs(n - d[bucket_index-1]) <= t:
                return True
            if bucket_index + 1 in d and abs(d[bucket_index+1] - n) <= t:
                return True
            d[bucket_index] = n
            if i >= k:
                index = getid(nums[i-k])
                d.pop(index)
        
        return False
