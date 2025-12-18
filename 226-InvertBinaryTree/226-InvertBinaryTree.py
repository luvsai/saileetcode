# Last updated: 18/12/2025, 20:19:12
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swap(self,node):
        if not node:
            return
        node.left , node.right = node.right, node.left
        self.swap(node.left)
        self.swap(node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swap(root)
        return root