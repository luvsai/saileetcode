# Last updated: 08/01/2026, 19:54:37
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights) ; n = len(heights[0])

        dist = [[float('inf')] * n for _ in range(m)]

        heap = [(0, 0,0)]# (effort  , startrow, startcol)

        dist [0][0] = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while heap:
            effort, r, c = heapq.heappop(heap)

            if (r,c) == (m-1,n-1):
                return effort #( which is min effort)
            
            if effort > dist[r][c] :
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr ,c + dc
                if 0<= nr < m and 0<=nc < n:
                    step_effort =  abs(heights[nr][nc] - heights[r][c])

                    # new_effort = effort + a_effort wrong
                    new_effort = max(effort, step_effort)

                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))
        return 0


