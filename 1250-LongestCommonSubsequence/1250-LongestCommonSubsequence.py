# Last updated: 18/12/2025, 20:17:15
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache
        def dfs(i, j):
            if i< 0 or j< 0:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + dfs(i-1,j-1)
            else:
                return max(dfs(i-1,j), dfs(i,j-1))
        
        # return dfs(len(text1)-1, len(text2) -1)

        # dynamic programming

        # dp[i][j] length of longest subsequence found between strings text1[:i] and text2[:j]
        # here when we compare we compare text1[i-1] and text2[j-1] so dp[i][j] talks text equal to i-1 and j-1 indexes
        m = len(text1) + 1
        n = len(text2) + 1
        dp = [[0 for _ in range(n )] for __ in range(m) ]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    if text1[i-1] == text2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

        # m = len(text1) + 1 
        # n = len(text2) + 1
        # dp = [0 for _ in range(n) ] 
        # for i in range(m):
        #     ndp = [0 for _ in range(n) ] 
        #     for j in range(n):
        #         if i == 0 or j == 0:
        #             ndp[j] = 0
        #         else:
        #             if text1[i-1] == text2[j-1]:
        #                 ndp[j] = dp[j-1] + 1
        #             else:
        #                 ndp[j] = max(dp[j], ndp[j-1])
        #     dp = ndp
        # return dp[-1]
