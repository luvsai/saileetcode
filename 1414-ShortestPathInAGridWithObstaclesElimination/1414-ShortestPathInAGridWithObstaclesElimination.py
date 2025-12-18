# Last updated: 18/12/2025, 20:17:14
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m , n = len(grid), len(grid[0])
        if k >= m + n -2:
            return m+ n -2
        
        visited = [[-1] * n for _ in range(m)] # remaining steps when visited the position
        visited[0][0] = k

        q = deque([(0,0,k,0)])
        DIR = [(1,0),(-1,0),(0,-1),(0,1)]
        while q:
            x,y ,rem,steps = q.popleft()

            # reached goal
            if x == m-1 and y == n-1:
                return steps
            for dx, dy in DIR:
                nx,ny = x+ dx , y + dy
                if 0 <= nx < m and 0 <= ny <n:
                    nk = rem - grid[nx][ny] # reduce k if cell is obstacle
                    if nk< 0:
                        continue
                    if visited[nx][ny] < nk:
                        visited[nx][ny] = nk
                        q.append((nx,ny,nk,steps+1))
            
        
        return -1