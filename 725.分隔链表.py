# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next

        q, r = l // k, l % k
        res = [None] * k
        cur = head
        for i in range(k):
            if not cur:
                break
            res[i] = cur
            cnt = q + (1 if i < r else 0)
            for _ in range(1, cnt):
                cur = cur.next
            next = cur.next
            cur.next = None
            cur = next

        return res


