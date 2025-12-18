# Last updated: 18/12/2025, 20:18:07
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m,n = len(grid) , len(grid[0])

        max_area = 0

        def dfs(r, c):
            if  (0 <= r <m) and (0 <= c<n) and grid[r][c] == 1:
                
                grid[r][c] = 0

                area = 1
                for dr, dc in [ (1,0),(0,1),(-1,0),(0,-1)] :
                    area += dfs(r + dr, c+ dc )
                return area
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1:
                    max_area = max(max_area,dfs(i,j))
        return max_area
            
