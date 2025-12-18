# Last updated: 18/12/2025, 20:18:40
from collections import deque
import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # m = len(heightMap) ; n = len(heightMap[0])
        # grid = heightMap
        

        # def bfs( level, grid, m,n):
        #     visited_dummy = [[False] * n for _ in range(m) ]
        #     q = deque()
        #     waterblocks=0
        #     for j in range(n):
        #         if grid[0][j] < level:
        #             visited_dummy[0][j] = True
        #             q.append((0,j))
        #         if grid[-1][j] < level:
        #             visited_dummy[-1][j] = True
        #             q.append((m-1,j))
        #     for i in range(1,m-1):
        #         if grid[i][0] < level:
        #             visited_dummy[i][0] = True
        #             q.append((i,0))
        #         if grid[i][-1] < level:
        #             visited_dummy[i][-1] = True
        #             q.append((i,n-1))
        #     while q:
        #         x,y = q.popleft()
        #         directions = [(0,1),(1,0),(-1,0),(0,-1)]
        #         for dx, dy in directions:
        #             nx , ny = x + dx, y + dy
        #             if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] < level and not visited_dummy[nx][ny]:
        #                 visited_dummy[nx][ny] = True
        #                 q.append((nx,ny))
            
        #     for i in range(m):
        #         for j in range(n):
        #             if visited_dummy[i][j] == False and grid[i][j] < level :
        #                 visited_dummy[i][j] = "****"

        #                 waterblocks +=1

        #     return waterblocks
        # final = 0
        # maxlevel = 0
        # for i in range(m):
        #     maxlevel = max(maxlevel , max(grid[i]))
        # for level in range(maxlevel,0,-1):
        #     final += bfs(level,grid,m,n)
        # return final

        #flood fill + heapq
        if not heightMap : return 0
        grid = heightMap

        m, n = len(grid), len(grid[0])

        heap = []
        visited = [[False] * n for _ in range(m)]

        # 1.Add all the borders to min-heap
        for i in range(m):
            for j in range(n):
                if i ==0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(heap, (grid[i][j], i , j))
                    visited[i][j] = True
        water = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        # Flood fill from the shortest wall
        while heap:
            h,x,y = heapq.heappop(heap)

            for dx, dy in directions:
                nx, ny = x+dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True

                    #If neighbor is lower=> water will be trapped!
                    if grid[nx][ny] < h:
                        water += h - grid[nx][ny]
                    #push with max current h and neighbor heigh
                    new_h = max(h, grid[nx][ny])
                    heapq.heappush (heap, (new_h, nx, ny))
        return water







# temp : [[1,4,3,1,3,2]
# [3,2,1,3,2,4]
# [2,3,3,2,3,1]]

# layer1 = [[1,4,3,1,3,2]
# [3,2,1,3,2,4]
# [2,3,3,2,3,1]]