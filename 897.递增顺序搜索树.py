# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode(-1)
        last = dummy
        def inorder(node):
            nonlocal last
            if not node:
                return
            inorder(node.left)

            last.right = node
            node.left = None
            last = node

            inorder(node.right)

        inorder(root)
        return dummy.right
