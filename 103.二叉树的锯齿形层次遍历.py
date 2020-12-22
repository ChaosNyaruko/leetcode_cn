#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        deq = collections.deque()
        deq.append(root)
        order = True # True:left->right False: right->left
        while deq:
            level = collections.deque()
            n = len(deq)
            for _ in range(n):
                cur = deq.popleft()
                if order:
                    level.append(cur.val)
                else:
                    level.appendleft(cur.val)
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)
            res.append(list(level))
            order = not order
        return res
        
                
            


# @lc code=end

