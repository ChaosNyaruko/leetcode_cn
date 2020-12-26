#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#
# https://leetcode-cn.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (78.53%)
# Likes:    589
# Dislikes: 0
# Total Accepted:    113.8K
# Total Submissions: 144.9K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
# 
# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL
# 的节点将直接作为新二叉树的节点。
# 
# 示例 1:
# 
# 
# 输入: 
# Tree 1                     Tree 2                  
# ⁠         1                         2                             
# ⁠        / \                       / \                            
# ⁠       3   2                     1   3                        
# ⁠      /                           \   \                      
# ⁠     5                             4   7                  
# 输出: 
# 合并后的树:
# 3
# / \
# 4   5
# / \   \ 
# 5   4   7
# 
# 
# 注意: 合并必须从两个树的根节点开始。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees_DFS(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        x = TreeNode(t1.val + t2.val)
        x.left = self.mergeTrees(t1.left, t2.left)
        x.right = self.mergeTrees(t1.right, t2.right)
        return x
    
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # BFS
        if not t1:
            return t2
        if not t2:
            return t1
        q = collections.deque()
        q1 = collections.deque()
        q2 = collections.deque()
        mergedRoot = TreeNode(t1.val + t2.val)
        q.append(mergedRoot)
        q1.append(t1)
        q2.append(t2)
        while q1 and q2:
            node = q.popleft()
            node1 = q1.popleft()
            node2 = q2.popleft()
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if left1 or left2:
                if left1 and left2:
                    left = TreeNode(left1.val + left2.val)
                    node.left = left
                    q.append(left)
                    q1.append(left1)
                    q2.append(left2)
                elif left1:
                    node.left = left1
                elif left2:
                    node.left = left2
            if right1 or right2:
                if right1 and right2:
                    right = TreeNode(right1.val + right2.val)
                    node.right = right
                    q.append(right)
                    q1.append(right1)
                    q2.append(right2)
                elif right1:
                    node.right = right1
                elif right2:
                    node.right = right2

        return mergedRoot



# @lc code=end

