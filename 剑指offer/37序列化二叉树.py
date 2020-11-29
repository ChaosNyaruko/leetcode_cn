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
            return "[]"
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                res.append(str(node.val))
            else:
                res.append("null")
        return '[' + ','.join(res)+']'


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        q = collections.deque()
        q.append(root)
        while q :
            node = q.popleft()
            # print(vals[i])
            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            # print(vals[i])
            if vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root)) 