"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(node):
            cur = node
            last = None
            while cur:
                next_ = cur.next

                if cur.child:
                    childLast = dfs(cur.child)

                    nxt = cur.next
                    cur.next = cur.child
                    cur.child.prev = cur

                    if nxt:
                        nxt.prev = childLast
                        childLast.next = nxt
                    cur.child = None
                    last = childLast
                else:
                    last = cur
                cur = next_
            
            return last
        dfs(head)
        return head
