# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        ans = 2 ** 32 - 1
        pre = -1
        def dfs(root):
            nonlocal ans, pre
            if root == None:
                return
            dfs(root.left)
            if pre == -1:
                pre = root.val
            else:
                ans = min(ans, root.val - pre)
                pre = root.val
            dfs(root.right)
            return
        dfs(root)
        return ans

