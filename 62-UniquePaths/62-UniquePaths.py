# Last updated: 08/01/2026, 19:57:52
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D dp array initialized to 1 for the first row and first column
        dp = [[1] * n for _ in range(m)]
        
        # Fill the dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # return dp[m-1][n-1] 
        return dp[-1][-1]