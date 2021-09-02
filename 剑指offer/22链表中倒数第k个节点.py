# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        while k > 0 and fast:
            fast = fast.next
            k -= 1

        while fast:
            slow = slow.next
            fast = fast.next

        return slow


