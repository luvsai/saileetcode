# Last updated: 18/12/2025, 20:17:41
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        all_visited = (1 << n ) - 1
        queue = deque()
        visited = set() # to avoid revisiting the same (node, mask). state

        #Initialize BFS from every node
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))
            visited.add((i,mask))
        
        while queue:
            node , mask , dist = queue.popleft()
            if mask == all_visited:
                return dist
            
            #Explore all the neighbors
            for nei in graph[node]:
                new_mask  = mask | (1 << nei) # Mark the neighbor as visited
                if (nei, new_mask) not in visited:
                    visited.add((nei, new_mask))
                    queue.append((nei, new_mask, dist+1))

