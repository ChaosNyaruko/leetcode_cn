#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right), 0)
        self.res = max(self.res, left + right + root.val)
        return max(left, right) + root.val
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -sys.maxsize - 1
        self.helper(root)
        return self.res
# @lc code=end

