#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        prefixFreq = dict()
        prefixFreq[0] = 1
        def helper(root, prefixSum):
            if not root:
                return
            prefixSum += root.val
            x = prefixSum - sum
            if x in prefixFreq:
                self.res += prefixFreq[x]
            if prefixSum in prefixFreq:
                prefixFreq[prefixSum] += 1
            else:
                prefixFreq[prefixSum] = 1
            
            helper(root.left, prefixSum)
            helper(root.right, prefixSum)
            prefixFreq[prefixSum] -= 1
            return
        helper(root, 0)
        return self.res
            
        
# @lc code=end

