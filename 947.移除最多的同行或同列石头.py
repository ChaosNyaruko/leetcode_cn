#
# @lc app=leetcode.cn id=947 lang=python3
#
# [947] 移除最多的同行或同列石头
#

# @lc code=start
class Solution:
    # def __init__(self):
    #     parent = dict()
    #     count = 0
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = dict()
        count = 0
        def find(x):
            nonlocal count
            if x not in parent:
                parent[x] = x
                count += 1
            if parent[x] != x: parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            nonlocal count
            rootx, rooty = find(x), find(y)
            if rootx == rooty:
                return
            parent[rootx] = rooty
            count -= 1
        for stone in stones:
            union(stone[0], ~stone[1])
            # print(count, parent)
        return len(stones) - count

# @lc code=end

