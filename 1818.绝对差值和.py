
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        a = nums1.copy()
        a.sort()
        n = len(nums1)
        mod = 1000000007
        s = 0
        maxn = 0
        for i in range(n):
            c = abs(nums1[i] - nums2[i])
            s = (s + c) % mod
            l, r = 0, n - 1
            # fine the first element that >= nums2[i]
            while l < r:
                m = l + (r - l) // 2
                if a[m] < nums2[i]:
                    l = m + 1
                else:
                    r = m

            #print("i=", i, "l=", l, "nums1[l]=", nums1[l], "nums2=", nums2[i])
            if a[l] >= nums2[i]:
                maxn = max(maxn, c - (a[l] - nums2[i]))
                if l > 0:
                    maxn = max(maxn, c - (nums2[i] - a[l - 1]))            
            else:
                #assert(nums2[i] > a[l])
                maxn = max(maxn, c- (nums2[i] - a[l]))
        #print(s)
        res = (s - maxn + mod) % mod
        return res
