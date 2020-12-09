#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast:
            if not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                cur = head
                while slow != cur:
                    slow = slow.next
                    cur = cur.next
                return cur
        return None
# @lc code=end

