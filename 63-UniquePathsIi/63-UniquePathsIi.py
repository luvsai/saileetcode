# Last updated: 08/01/2026, 19:57:50
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == 1:
            return 0 # no way to start the path
        dp = [[ 0 ] *n for _ in range(m) ] # O(mxn)

        # base condition
        dp[0][0 ] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                if j >0 :
                    dp[i][j] += dp[i][j-1]
                if i > 0:
                    dp[i][j] += dp[i-1][j]
        return dp[-1][-1]