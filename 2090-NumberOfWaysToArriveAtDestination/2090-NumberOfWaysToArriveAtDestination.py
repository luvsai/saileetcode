# Last updated: 18/12/2025, 20:16:55
from collections import defaultdict
import heapq
MOD = 10 ** 9 + 7
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for road in roads:
            u , v, w = road[0] , road[1], road[2]
            adj [u].append((v,w))
            adj[v] .append((u, w))

        minheap = []

        timefsrc = [float('inf')] * n
        ways = [0] * n
        

        src = 0
        timefsrc [src] = 0
        ways[src] = 1
        dest = n-1

        minheap .append((0, src))
        while minheap:
            ctime , node = heapq. heappop(minheap)

            if ctime > timefsrc[node]:
                continue
            for neighbor in adj[node] :
                neighbornode, timetn = neighbor[0], neighbor[1]
                newtime = ctime + timetn
                if ( newtime ) < timefsrc[neighbornode]:
                    timefsrc[neighbornode] = newtime
                    ways[neighbornode] = ways[node]
                    heapq.heappush(minheap, (newtime, neighbornode))
                elif newtime == timefsrc[neighbornode]:
                    ways[neighbornode] = (ways[node] + ways[neighbornode] ) % MOD
                
        return ways[dest] % MOD
