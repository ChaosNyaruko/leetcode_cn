# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                yield root.val

            yield from dfs(root.left)
            yield from dfs(root.right)


        seq1 = list(dfs(root1))
        seq2 = list(dfs(root2))
        return seq1 == seq2




