# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = []
        def dfs(node, row, col):
            if not node:
                return
            
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        res = []
        last = float('-inf')
        nodes.sort()
        for col, row, val in nodes:
            if col != last:
                res.append([])
                last = col
            res[-1].append(val)

        return res

