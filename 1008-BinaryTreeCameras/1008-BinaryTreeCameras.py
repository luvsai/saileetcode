# Last updated: 18/12/2025, 20:17:27
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
                # Using 3 colors: 0,1,2
        self.cameras = 0

        def dfs(node):
            if not node:
                return 1 # null nodes are covered
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left ==0 or right ==0:
                # place camera
                self.cameras +=1
                return 2 # camera placed
            if left ==2 or right == 2:
                # covered
                return 1
            

            return 0 # not convered.
        if dfs(root) == 0:
            self.cameras +=1
        return self.cameras



        # return 0
######
# Wrong assumption

        # colorcount = {0:0, 1:0}
        # def dfs(node, ncolor):
        #     if not node:
        #         return 
        #     #color the node with the colorand increment the color count
        #     colorcount[ncolor] +=1

        #     #ask the left and right children to color themselves with negated color
        #     nncolor = 1- ncolor
        #     dfs(node.left,nncolor)
        #     dfs(node.right, nncolor)
        # dfs(root, 1)
        # vals = colorcount.values()
        # print(vals)
        # if 0 in vals:
        #     return max(vals)
        # return min(colorcount.values())

        