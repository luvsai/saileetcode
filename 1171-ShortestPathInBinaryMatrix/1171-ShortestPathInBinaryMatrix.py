# Last updated: 18/12/2025, 20:17:18
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # if start or end is blocked no path
        if grid[0][0] == 1 or grid[n - 1][n - 1] :
            return -1
        visited = set()
        visited.add((0,0))

        # BFS Queue , row, col , distance
        q = deque([(0,0,1)])
        directions = [
            (1,0),(0,1),(-1,0),(0,-1)
            ,(1,1),(-1,-1),(-1,1),(1,-1)
        ]

        while q:
            x, y , dist = q.popleft()

            # reached destination
            if x == (n-1) and y == (n-1):
                return dist
            
            # explore neighbors
            for dx, dy in directions:
                nx , ny = x + dx, y + dy
                if 0<= nx < n and 0<= ny < n and (nx, ny) not in visited and grid[nx][ny] == 0:
                    visited.add((nx, ny))
                    q.append((nx,ny, dist +1))
        return -1
        


        