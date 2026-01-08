# Last updated: 08/01/2026, 19:57:22
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        lookup = [[False] * n for _  in range(n) ]


        #base condition
        for i in range(n):
            lookup[i][i] = True
       
       
        # o(n2) to create the table and o(1) for futher lookups
        for length in range(2, n+ 1):
            for i in range(n - length+ 1):
                j = i + length -1
                if s[i] == s[j]:
                    if length <=3 :
                        lookup[i][j] = True
                    elif lookup[i+1][j -1]:
                        lookup[i][j] = True
                   
        #
        mincuts = float('inf')
       


        # O(n2)
        # print (lookup)
       
        # dp = {}
        # def dfs(j):
        #     if j in dp:
        #         return dp[j]
        #     if j >=n :
        #         return 0
        #     if lookup[j][n-1]:
        #         return 0
        #     minways = float('inf')
        #     for k in range(j,n ):
        #         if lookup[j][ k ]  :
        #             minways = min(1 + dfs(k + 1), minways)
        #     dp[j]  = minways
        #     return minways


        # mincuts = dfs(0)
        dp = [0] * (n + 1)
        dp[n] = 0
        for j in range(n-1, -1, -1):
            if lookup[j][n-1]:
                dp[j] = 0
                continue
            minways = float('inf')
            for k in range(j, n):
                if lookup[j][k]:
                    minways = min(minways, 1+ dp[k+1])
            dp[j] = minways




        return dp[0]