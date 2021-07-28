# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = dict()
        def findParent(node):
            if node.left:
                parents[node.left] = node
                findParent(node.left)

            if node.right:
                parents[node.right] = node
                findParent(node.right)

        res = []
        def dfs(node, source, depth):
            if not node:
                return
            if depth == k:
                res.append(node.val)
                return

            if node.left != source:
                dfs(node.left, node, depth + 1)

            if node.right != source:
                dfs(node.right, node, depth + 1)

            if node in parents and parents[node] != source:
                dfs(parents[node], node, depth + 1)

            return
        findParent(root)
        dfs(target, None, 0)

        return res

