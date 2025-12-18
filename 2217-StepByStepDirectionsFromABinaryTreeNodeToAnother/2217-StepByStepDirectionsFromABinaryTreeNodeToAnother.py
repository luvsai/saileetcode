# Last updated: 18/12/2025, 20:16:53
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, path, target):
        if node.val == target:
            return True
        # print(node.val)
        if node.left and self.dfs(node.left , path, target):
            path.insert(0,"L")
            return True
        if node.right and self.dfs(node.right , path, target):
            path.insert(0,"R")
            return True
        return False

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # do the dfs search
        pathtoSt = []
        pathtoDt = []
        
        self.dfs(root, pathtoSt, startValue)
        self.dfs(root,pathtoDt,destValue)
        # print(pathtoSt, pathtoDt)
        i = 0
        while i < len(pathtoSt) and i < len(pathtoDt) and pathtoSt[i] == pathtoDt[i] :
            i +=1
        
        ups = "U" * (len(pathtoSt) - i )
        final = ups + "".join(pathtoDt[i:])
        return final
