# Last updated: 18/12/2025, 20:18:00
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        # Distance array
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # Min-heap: (distance, node)
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)
            
            # If this distance is not optimal anymore
            if time > dist[node]:
                continue
            
            for nei, wt in adj[node]:
                new_time = time + wt
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap, (new_time, nei))
        
        # Find max distance among all reachable nodes
        max_dist = max(dist[1:])
        return -1 if max_dist == float('inf') else max_dist