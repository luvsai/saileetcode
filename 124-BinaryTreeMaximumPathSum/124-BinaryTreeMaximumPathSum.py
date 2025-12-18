# Last updated: 18/12/2025, 20:19:53
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxpathsum = float("-inf")

    def traverse2(self,node):
        if not node :
            return 0
        lv = max(self.traverse2(node.left),0)
        #* dont return negative sum to root from leaves or at roots if child returns a -negative value discard it and use 0
        rv = max(self.traverse2(node.right),0)
        currentmxp = node.val +  lv + rv
        self.maxpathsum= max(self.maxpathsum, currentmxp)
        return max(lv,rv) + node.val

    def traverse (self,node):
        if not node : 
            return 0
        lv = self.traverse(node.left)
        rv = self.traverse(node.right)
        if lv < 0:
            lv = 0
        if rv< 0:
            rv = 0
        
        csum= lv + rv + node.val
        self.maxpathsum = max(self.maxpathsum, csum)

        return max(lv, rv) + node.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.traverse2(root)
        return self.maxpathsum