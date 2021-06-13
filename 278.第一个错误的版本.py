# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        # 找到最早的true
        while l < r:
            m = l + (r- l)//2
            if not isBadVersion(m):
                l = m + 1
            else:
                r = m

        return l 

