# Last updated: 18/12/2025, 20:17:46
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return False
            ltr = dfs(node.left)
            rtr = dfs(node.right)
            if not ltr:
                node.left = None
            if not rtr:
                node.right = None

            if node.val == 0 and (not ltr) and (not rtr):
                return False
            return True
        result =  dfs(root) 
        if not result:
            return None
        return root

            
