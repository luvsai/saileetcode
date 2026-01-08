# Last updated: 08/01/2026, 19:54:46
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 **9 + 7
        self.max_product = 0
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        total = totalSum(root)

        #Step 2
        def dfs(node):
            # at every index find the sum below left sum + right sum + nodeval  -> x
            # compute (Sum - x) * x and update with the max (self.max_product)
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            currtreesum = left + right + node.val
            self.max_product = max(self.max_product , (currtreesum * (total - currtreesum)) ) 
            
            return currtreesum
        dfs(root)
        return self.max_product % MOD



        