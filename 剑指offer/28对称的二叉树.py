# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, p1, p2) ->bool:
        if not p1:
            return not p2
        if not p2:
            return not p1
        if p1.val != p2.val:
            return False
        return self.helper(p1.left, p2.right) and self.helper(p1.right, p2.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)