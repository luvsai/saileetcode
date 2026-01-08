# Last updated: 08/01/2026, 19:55:00
#🔑 Key Takeaways (Memorize These)

# Two-phase problems need two algorithms

# DFS = identify region

# Multi-source BFS = shortest distance between regions

# BFS layers = number of flips

# First hit = optimal answer

from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1,0), (0,1),(-1,0),(0,-1)]

        visited = [[False]* n for _ in range(n)]


        q = deque()

        # phase 1 : DFS to find the first island
        def dfs(r,c):
            if r<0 or r>=n or c< 0 or c>= n:
                return
            if visited[r][c] or grid[r][c] == 0:
                return
            visited[r][c] = True
            q.append((r,c))
            for dx,dy in directions:
                dfs(r + dx , c + dy)
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    found = True
                    break
        
        #phase 2 mutli source bfs
        steps = 0

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+ dr, c + dc
                    if 0<= nr< n and 0<= nc < n and not visited[nr][nc]:
                        if grid[nr][nc] == 1:
                            return steps # second island reached
                        visited[nr][nc] = True
                        q.append((nr,nc))
            steps +=1

        return steps

