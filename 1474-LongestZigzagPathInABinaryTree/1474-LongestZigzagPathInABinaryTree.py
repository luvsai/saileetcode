# Last updated: 18/12/2025, 20:17:13
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return (-1,-1)
            left = dfs(node.left)
            right = dfs(node.right)
            
            go_left = 1 + left[1] # left child, but before move must be right
            go_right = 1 + right[0] # right chld, but before move must be left

            self.ans = max(self.ans, go_left, go_right)
            return (go_left, go_right)
        dfs(root)
        return self.ans




