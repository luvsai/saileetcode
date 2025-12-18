# Last updated: 18/12/2025, 20:17:43
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # steps
        # color each island with a digit starting from 2:
        # for every island colored keep track of the area of the island in a hasmap key is color and value is area.
        # for every 0 present in the left over grid. peak into the 4 neighbors and if land than add the areas of the lands and + 1 flipping 0 and track the maximum of such areas found
        #return the maximum area
        
        maxarea = 0
        n = len(grid) # a square grid    
        island_color = 2
        size  = {}
        from collections import deque
        def bfs(r,c, id):
            grid[r][c] = id
            count = 1
            q = deque([(r,c)])
            while q:
                x, y = q.popleft()
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0<= nx< n and 0<= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = id # coloring the island
                        count +=1
                        q.append((nx,ny))
            
            return count
        # color each island with a digit starting from 2:
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    count = bfs(i,j,island_color)
                    maxarea = max(maxarea, count)
                    size[island_color] = count
                    island_color +=1
        
        #step2:
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    directions = [(1,0),(0,1),(-1,0),(0,-1)]
                    seen = set()
                    area = 1# flipping the cell
                    for dx , dy in directions:
                        nx = i  + dx; ny = j + dy
                        if 0<= nx< n and 0<= ny < n and grid[nx][ny] >1:
                            id = grid[nx][ny]
                            if id not in seen:
                                seen.add(id)
                                area += size[id]
                    maxarea = max(maxarea,area)
        return maxarea