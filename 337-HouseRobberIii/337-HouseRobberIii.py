# Last updated: 18/12/2025, 20:18:45
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0,0) #(rob, not_rob)
            left = dfs(node.left)
            right = dfs(node.right)

            # rob this node not_rob of left and right
            rob = node.val + left[1] + right[1]

            # not rob you can choose rob / not rob max value 
            not_rob = max(left) + max(right)

            return (rob, not_rob)
        return max(dfs(root))