# Last updated: 18/12/2025, 20:20:04
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkhb(self,node):
        if not node:
            return 0 , True
        left , lf = self.checkhb(node.left)
        right , rf = self.checkhb(node.right)
        if not lf or not rf:
            return max(left, right) + 1 , False

        return max(left, right) + 1, abs(left -right) <= 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        mh, stat = self.checkhb(root)
        return stat
        