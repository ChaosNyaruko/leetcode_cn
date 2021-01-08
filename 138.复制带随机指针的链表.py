#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        p = head
        while p:
            copy = Node(p.val, p.next, None)
            p.next = copy
            p = copy.next

        #connect random pointer
        p = head
        while p:
            if not p.random:
                p.next.random = None
            else:
                p.next.random = p.random.next
            p = p.next.next

        p = head
        res = p
        # connect next  pointer
        if not p:
            res = None
        else:
            res = p.next
        while p:
            copy = p.next
            p.next = copy.next
            if p.next:
                copy.next = p.next.next
            else:
                copy.next = None
            p = p.next
        return res

# @lc code=end

