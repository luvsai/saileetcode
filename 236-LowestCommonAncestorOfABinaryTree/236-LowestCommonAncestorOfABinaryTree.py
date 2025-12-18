# Last updated: 18/12/2025, 20:19:07
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self,node, p, q):
        if not node:
            return None
        if node.val == p or node.val == q:
            return node
        left = self.dfs(node.left,p,q)
        right = self.dfs(node.right,p,q)
        if left and right:
            return node
        if left:
            return left
        if right:
            return right
        return None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root,p.val,q.val)
        