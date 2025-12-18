# Last updated: 18/12/2025, 20:17:16
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        rootNodes = []
        to_dset = set(to_delete)
        def refreshForest(node,isroot):
            if isroot and node.val not in to_dset:
                rootNodes.append(node)
                isroot = False
            if node.val in to_dset:
                isroot = True
            if node.left :
                tmp = node.left
                if node.left.val in to_dset:
                    node.left = None
                
                refreshForest(tmp, isroot)
                
            if node.right:
                tmp = node.right
                if node.right.val in to_dset:
                    node.right = None
                    
                refreshForest(tmp,isroot)
                
        refreshForest(root, True)
        return rootNodes
                
            
        