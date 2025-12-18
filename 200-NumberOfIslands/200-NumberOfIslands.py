# Last updated: 18/12/2025, 20:19:26
from collections import deque
from typing import List

class Solution:
    def bfs(self, i: int, j: int, grid: List[List[str]], vis: List[List[bool]], V: int, W: int):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque([(i, j)])
        vis[i][j] = True
        
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                ni, nj = x + dx, y + dy
                if 0 <= ni < V and 0 <= nj < W and not vis[ni][nj] and grid[ni][nj] == "1":
                    vis[ni][nj] = True
                    q.append((ni, nj))
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        V, W = len(grid), len(grid[0])
        vis = [[False] * W for _ in range(V)]
        islands = 0
        
        for i in range(V):
            for j in range(W):
                if grid[i][j] == "1" and not vis[i][j]:
                    self.bfs(i, j, grid, vis, V, W)
                    islands += 1
        
        return islands