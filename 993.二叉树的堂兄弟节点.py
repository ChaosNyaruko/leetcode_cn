# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_parent, x_depth, x_found = None, 0, False
        y_parent, y_depth, y_found = None, 0, False
        def dfs(node, depth, parent):
            if not node:
                return

            nonlocal x_parent, x_depth, x_found
            nonlocal y_parent, y_depth, y_found

            if node.val == x:
                x_parent, x_depth, x_found = parent, depth, True
            elif node.val == y:
                y_parent, y_depth, y_found = parent, depth, True

            if x_found and y_found:
                return

            dfs(node.left, depth + 1, node)

            if x_found and y_found:
                return

            dfs(node.right, depth + 1, node)

        dfs(root, 0, None)
        return x_depth == y_depth and x_parent != y_parent



