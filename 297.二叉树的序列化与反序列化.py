#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#@"
        res = str(root.val) + "@"
        return res + self.serialize(root.left) + self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split("@")
        # print("data", data, "nodes", nodes)
        
        def helper(l: List[str]):
            if not nodes:
                return None
            if l[0] == '#':
                l.pop(0)
                return None
            cur = TreeNode(int(l[0]))
            l.pop(0)

            cur.left = helper(l)
            cur.right = helper(l)
            return cur
        return helper(nodes)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

