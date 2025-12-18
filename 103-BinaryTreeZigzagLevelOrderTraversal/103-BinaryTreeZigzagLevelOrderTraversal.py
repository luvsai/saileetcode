# Last updated: 18/12/2025, 20:20:10
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        flag = True
        q = deque([root])
        answer = []
        while q:
            qlen = len(q)
            level = []
            if flag:
                for _ in range(qlen):

                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            else:
                for _ in range(qlen):

                    node = q.pop()
                    level.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                    
            answer.append(level)
            flag = not flag

        return answer

        