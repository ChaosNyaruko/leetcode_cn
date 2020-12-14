#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        slow = head
        fast = head

        # 退出循环是slow是列表的中点（奇数）或者上半个列表的末尾（偶数）
        # 以fast过滤是不使slow变成下半列表的起点？
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        nextStart = slow.next
        # print(slow.val, nextStart.val)

        # reverse nextStart
        cur  = nextStart
        prev = None
        while cur:
            curNext = cur.next
            cur.next = prev
            prev = cur
            cur = curNext

        h1, h2 = head, prev
        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next

        return True


# @lc code=end

