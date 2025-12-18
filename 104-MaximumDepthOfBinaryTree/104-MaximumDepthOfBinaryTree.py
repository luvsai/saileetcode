# Last updated: 18/12/2025, 20:20:08
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        left = right = 0
        if node.left :
            left = self.dfs(node.left)
        if node.right:
            right = self.dfs(node.right)
        return max(left, right) + 1
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
        