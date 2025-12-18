# Last updated: 18/12/2025, 20:18:18
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxima = 0
    def findlrhsum(self,node):
            if not node: 
                return 0
            lh = self.findlrhsum(node.left)
            rh = self.findlrhsum(node.right)

            hsum = lh + rh
            self.maxima = max(self.maxima, hsum)
            return max(lh , rh) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.findlrhsum(root)
        return self.maxima
        