"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node: 'Node'):
            if not node:
                return
            helper(node.left)
            if self.pre:
                self.pre.right = node
                node.left = self.pre
            else:
                self.head = node
            self.pre = node
            helper(node.right)
        if not root:
            return None
        self.pre = None
        helper(root)
        # 形成环状链表
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
        