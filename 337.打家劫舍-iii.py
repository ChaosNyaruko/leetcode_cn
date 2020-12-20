#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = dict()
        def helper(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            res = 0 
            if root.left:
                res += helper(root.left.left) + helper(root.left.right)
            if root.right:
                res += helper(root.right.left) + helper(root.right.right)
            
            # steal root
            r1 = root.val + res
            # do not steal root
            r2 = helper(root.left) + helper(root.right)
            memo[root] = max(r1, r2)
            return memo[root]
        return helper(root)

        
# @lc code=end

