# Last updated: 18/12/2025, 20:17:48
# from collections import deque
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         nrange = range(n)
#         adj = [[] for _ in nrange]
#         for it in flights:
#             adj[it[0]].append((it[1],it[2]))
#         q = deque([])
#         dis = [float('inf')] * n
#         dis[src] = 0
#         q.append((0, src, 0))
#         while q:
#             print(q)
#             stop , node, distance = q.popleft()
#             if stop > k + 1:
#                 return -1
#             for (neighbor, ndistance) in adj[node]:
#                 nndis = distance + ndistance
#                 if nndis < dis[neighbor] and stop <= k:
#                     dis[neighbor] = nndis
#                     q.append((stop + 1, neighbor, nndis))
#         if dis[dst] == float('inf'):
#             return -1
#         return dis[dst]

from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append((v, cost))
        
        q = deque()
        dis = [float('inf')] * n
        dis[src] = 0
        
        # (stops, node, total_cost)
        q.append((0, src, 0))
        
        while q:
            stops, node, total_cost = q.popleft()
            
            # Don't explore beyond k stops
            if stops > k:
                continue
            
            for neighbor, price in adj[node]:
                new_cost = total_cost + price
                if new_cost < dis[neighbor]:
                    dis[neighbor] = new_cost
                    q.append((stops + 1, neighbor, new_cost))
        
        return dis[dst] if dis[dst] != float('inf') else -1
