# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0, head)
        prevp = dummy
        p = head
        k = left
        while k > 1:
            prevp = p
            p = p.next
            k -= 1

        def reverse(head, k):
            # print("in reverse", k, head.val)
            prev = None
            cur = head
            while k:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
                k -= 1
            # prev is new head
            return prev, cur

        nhead, nnext = reverse(p, right - left + 1)
        # print("nhead:%d, nnext:%d"% (nhead.val, nnext.val))

        prevp.next = nhead
        p.next = nnext
        return dummy.next


