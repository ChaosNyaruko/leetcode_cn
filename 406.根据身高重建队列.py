#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort people by height inc
        # ki desc
        def cmp(person):
            return -person[0], person[1]

        people.sort(key=cmp)
        print("after sort", people)
        res = []
        for person in people:
            res.insert(person[1], person)
            # print("res", res)
        
        return res

# @lc code=end

