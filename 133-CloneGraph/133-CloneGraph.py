# Last updated: 18/12/2025, 20:19:48
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {node: Node(node.val)} # this only holds the reference node key old node adress value is new node address end we use old node as key and return new node value .
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for nei in curr.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    queue.append(nei)
                old_to_new[curr].neighbors.append(old_to_new[nei])
        
        return old_to_new[node]