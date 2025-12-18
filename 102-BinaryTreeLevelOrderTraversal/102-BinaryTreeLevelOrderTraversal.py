# Last updated: 18/12/2025, 20:20:11
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root :
        #     return []
        # queue = deque([root])
        # final = []
        # while queue:
        #     qlen = len(queue)
        #     auxarr = []
        #     for _ in range(qlen):
        #         node = queue.popleft()
                
        #         auxarr.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     final.append(auxarr)
        # return final
        res = []
        
        def dfs(node, depth):
            if not node:
                return
            
            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return res
        
        