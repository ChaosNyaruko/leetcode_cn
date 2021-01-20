#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cnt = 0
        res = -1
        def dfs(node):
            nonlocal cnt, res
            if not node:
                return
            dfs(node.left)
            cnt += 1
            if cnt == k:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res

# @lc code=end

