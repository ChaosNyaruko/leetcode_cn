# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        slow = head
        n = 1
        while slow.next:
            n += 1
            slow = slow.next
        
        k = k % n
        if k == 0:
            return head
        slow = fast = head
        while k:
            k -= 1
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        ret = slow.next
        slow.next = None
        fast.next = head
        return ret
