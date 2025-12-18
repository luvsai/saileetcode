# Last updated: 18/12/2025, 20:18:46
from collections import defaultdict
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list) 

#        build graph with min heaps
        for src, dst in tickets:
            heapq.heappush(graph[src] , dst)
        
        route = []
        def dfs(airport):
            while graph[airport] :
                next_dst = heapq.heappop(graph[airport])
                dfs(next_dst)
            route.append(airport)
        dfs("JFK")
        return route[::-1]
           