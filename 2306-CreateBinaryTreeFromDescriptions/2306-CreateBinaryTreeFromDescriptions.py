# Last updated: 18/12/2025, 20:16:50
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hasmap = dict()
        children = set()
        for description in descriptions:
            if hasmap.get(description[0]) :
                node = hasmap[description[0]]
            else :
                node =  TreeNode(val=description[0])
                hasmap[description[0]] = node
            if description[2] == 1:
                if hasmap.get(description[1]) :
                    node.left =  hasmap[description[1]]
                else :
                    node.left = TreeNode(val=description[1])
                    hasmap[description[1]] = node.left
                    
            else:
                if hasmap.get(description[1]) :
                    node.right =  hasmap[description[1]]
                else :
                    node.right = TreeNode(val=description[1])
                    hasmap[description[1]] = node.right
            children.add(description[1]) 
        rootval = None 
        for val in hasmap:
            if val not in children:
                rootval = val
        # print(hasmap)
        print(rootval)
        return hasmap[rootval]

        
        
        