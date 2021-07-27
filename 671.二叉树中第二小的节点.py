# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res, m = -1, root.val
        def dfs(root):
            nonlocal res
            if not root:
                return

            if res != -1 and root.val >= res:
                return

            if root.val > m:
                res = root.val

            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
