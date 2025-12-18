# Last updated: 18/12/2025, 20:18:57
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
            return ""
        from collections import deque
        q = deque([root])
        res = []

        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))

        from collections import deque
        q = deque([root])
        i = 1
        while q and i < len(values):
            node = q.popleft()
            #left 
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i +=1

            #right
            if i < len(values) and values[i] != "null" :
                node.right = TreeNode (int(values[i]))
                q.append(node.right)
            i += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))